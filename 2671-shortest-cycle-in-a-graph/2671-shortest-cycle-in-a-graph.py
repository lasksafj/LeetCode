class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res = inf
        dist = [inf]*n
        def dfs(i, p, d):
            nonlocal res
            dist[i] = d
            for ne in adj[i]:
                if ne == p: continue
                if dist[ne] > d+1:
                    dfs(ne, i, d+1)
                elif dist[ne] < dist[i]:
                    res = min(res, dist[i] - dist[ne] + 1)

        for i in range(n):
            if dist[i] < inf: continue
            dfs(i, -1, 0)
            
        return res if res < inf else -1