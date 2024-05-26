class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        P = sorted(list(range(n)), key=lambda i:disappear[i])
        adj = defaultdict(list)
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w))
        pq = [[0,0]]
        vis = [inf]*n
        vis[0] = 0
        j = 0
        while pq:
            t,cur = heappop(pq)
            if t > vis[cur]:
                continue
            while j < len(P) and t >= disappear[P[j]]:
                if P[j] in adj:
                    del adj[P[j]]
                j += 1
            for ne,w in adj[cur]:
                if ne not in adj:
                    continue
                if t+w >= disappear[ne]:
                    continue
                if t+w < vis[ne]:
                    vis[ne] = t+w
                    heappush(pq, [t+w, ne])
        return [v if v < inf else -1 for v in vis]