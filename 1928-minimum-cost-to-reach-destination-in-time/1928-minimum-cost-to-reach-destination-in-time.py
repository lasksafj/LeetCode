class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        adj = defaultdict(list)
        for a,b,c in edges:
            adj[a].append([b,c])
            adj[b].append([a,c])
        n = len(passingFees)
        pq = [[passingFees[0], 0, 0]]
        time = [inf]*n
        time[0] = 0
        while pq:
            c, t, u = heappop(pq)
            if u == n-1:
                return c
            for v,d in adj[u]:
                if time[v] > t + d and t + d <= maxTime:
                    time[v] = t + d
                    heappush(pq, [c + passingFees[v], t + d, v])
        return -1