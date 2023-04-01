class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res = 9999
        for i in range(n):
            dist = [9999]*n
            f = [-1]*n
            q = deque([i])
            dist[i] = 0
            while q:
                c = q.popleft()
                for ne in adj[c]:
                    if dist[ne] == 9999:
                        dist[ne] = dist[c] + 1
                        f[ne] = c
                        q.append(ne)
                    elif f[c] != ne:
                        res = min(res, dist[ne] + dist[c] + 1)
        return res if res < 9999 else -1