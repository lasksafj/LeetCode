class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res = inf
        for i in range(n):
            dist = [inf]*n
            f = [-1]*n
            q = deque([i])
            dist[i] = 0
            while q:
                c = q.popleft()
                for ne in adj[c]:
                    if ne == f[c]: continue
                    if dist[ne] == inf:
                        dist[ne] = dist[c] + 1
                        f[ne] = c
                        q.append(ne)
                    else:
                        res = min(res, dist[ne] + dist[c] + 1)
        return res if res < inf else -1