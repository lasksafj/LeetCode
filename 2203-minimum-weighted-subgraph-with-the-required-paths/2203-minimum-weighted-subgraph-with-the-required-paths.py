class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def F(adj, src):
            pq = [(0,src)]
            dist = [inf]*n
            dist[src] = 0
            while pq:
                d,u = heappop(pq)
                if d > dist[u]:
                    continue
                for v,w in adj[u]:
                    if dist[v] > d+w:
                        dist[v] = d+w
                        heappush(pq, (d+w, v))
            return dist
        adj = [[] for _ in range(n)]
        radj = [[] for _ in range(n)]
        for a,b,w in edges:
            adj[a].append((b,w))
            radj[b].append((a,w))
        dist1 = F(adj, src1)
        dist2 = F(adj, src2)
        dist3 = F(radj, dest)
        res = inf
        for i in range(n):
            res = min(res, dist1[i] + dist2[i] + dist3[i])
        return res if res < inf else -1