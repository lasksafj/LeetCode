class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        numbering = [-1] * n
        low = [-1] * n
        
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
            
        res = []
        cnt = [0]
        def dfs(cur, prev):
            numbering[cur] = cnt[0]
            low[cur] = cnt[0]
            cnt[0] += 1
            for v in adj[cur]:
                # print(cur, v, low[cur], numbering[v])
                if numbering[v] == -1:
                    dfs(v, cur)
                    low[cur] = min(low[cur], low[v])
                elif v != prev:
                    low[cur] = min(low[cur], numbering[v])
                if numbering[cur] < low[v]:
                    res.append([cur, v])
                    
        
        # for i in range(n):
        #     if numbering[i] == -1:
        #         dfs(i, -1)
        dfs(0, -1)
        return res
            