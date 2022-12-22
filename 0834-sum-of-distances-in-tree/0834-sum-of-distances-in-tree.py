class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        cnt = [0] * n
        stsum = [0] * n
        
        def dfs(prev, cur):
            cnt[cur] = 1
            for ne in adj[cur]:
                if ne != prev:
                    dfs(cur, ne)
                    cnt[cur] += cnt[ne]
                    stsum[cur] += stsum[ne] + cnt[ne]
        
        dfs(-1, 0)
        res = [0] * n
        res[0] = stsum[0]
        def dfs2(prev, cur):
            if cur != 0:
                res[cur] = res[prev] + (n - cnt[cur]) - cnt[cur]
            for ne in adj[cur]:
                if ne != prev:
                    dfs2(cur, ne)
        
        dfs2(-1, 0)
        return res