class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w*2))
        pq = [(0,0)]
        dist = [inf]*n
        dist[0] = 0
        while pq:
            cur,a = heappop(pq)
            if cur > dist[a]: continue
            for b,w in adj[a]:
                if dist[b] > cur+w:
                    dist[b] = cur+w
                    heappush(pq, (cur+w, b))
        return dist[n-1] if dist[n-1] < inf else -1