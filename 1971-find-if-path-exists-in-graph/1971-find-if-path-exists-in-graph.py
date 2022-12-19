class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis = [False] * (n+1)
        adj = [[] for _ in range(n+1)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i):
            if i == destination:
                return True
            vis[i] = True
            for nv in adj[i]:
                if not vis[nv]:
                    if dfs(nv):
                        return True
            return False
        return dfs(source)