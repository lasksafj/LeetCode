class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        adj = defaultdict(list)
        n = len(online)-1
        ma = 0
        for a,b,c in edges:
            if online[a] and online[b]:
                adj[a].append([b,c])
            ma = max(ma, c)
        def check(x):
            @cache
            def dfs(i):
                if i == n:
                    return 0
                res = inf
                for ne,c in adj[i]:
                    if c >= x:
                        res = min(res, c + dfs(ne))
                return res
            return dfs(0) <= k
        l,r = 0,ma
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                l = mi+1
            else:
                r = mi-1
        
        return r