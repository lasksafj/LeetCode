class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)
        P = sorted(list(range(N)), key=lambda i:wage[i]/quality[i])
        pq = []
        s = 0
        for i in range(k):
            heappush(pq, -quality[P[i]])
            s += quality[P[i]]
        res = wage[P[k-1]]/quality[P[k-1]] * s
        for i in range(k,N):
            q = -heappop(pq)
            s -= q
            heappush(pq, -quality[P[i]])
            s += quality[P[i]]
            res = min(res, wage[P[i]]/quality[P[i]] * s)
        
        return res
            