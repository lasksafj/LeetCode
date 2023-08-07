class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj = [[0]*n for _ in range(n)]
        deg = [0]*n
        for a,b in edges:
            adj[a-1][b-1] = 1
            adj[b-1][a-1] = 1
            deg[a-1] += 1
            deg[b-1] += 1
        res = inf
        for v1 in range(n):
            for v2 in range(v1+1, n):
                if adj[v1][v2]:
                    for v3 in range(v2+1, n):
                        if adj[v1][v3] and adj[v2][v3]:
                            res = min(res, deg[v1] + deg[v2] + deg[v3] - 6)
        return res if res < inf else -1