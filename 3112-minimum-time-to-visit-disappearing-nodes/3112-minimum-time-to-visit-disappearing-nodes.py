class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj = defaultdict(list)
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w))
        pq = [[0,0]]
        vis = [inf]*n
        vis[0] = 0
        while pq:
            t,cur = heappop(pq)
            if t > vis[cur]:
                continue
            for ne,w in adj[cur]:
                if t+w < vis[ne] and t+w < disappear[ne]:
                    vis[ne] = t+w
                    heappush(pq, [t+w, ne])
        return [v if v < inf else -1 for v in vis]