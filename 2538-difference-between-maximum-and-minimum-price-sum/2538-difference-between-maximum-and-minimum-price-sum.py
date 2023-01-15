class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        @cache
        def dfs(cur,prev):
            res = 0
            for ne in adj[cur]:
                if ne != prev:
                    res = max(res, dfs(ne,cur))
            return res + price[cur]
        res = 0
        for i in range(n):
            ma = dfs(i,-1)
            res = max(res, ma-price[i])
        return res
                    
            