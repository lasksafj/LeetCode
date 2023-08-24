class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        A = sorted(intervals)
        res = {}
        i = 0
        pq = []
        for q in sorted(queries):
            while i < len(A) and A[i][0] <= q:
                l,r = A[i]
                heappush(pq, (r-l+1, r))
                i += 1
            while pq:
                size,r = pq[0]
                if r < q:
                    heappop(pq)
                else:
                    break
            if pq:
                res[q] = pq[0][0]
            else:
                res[q] = -1
        return [res[q] for q in queries]