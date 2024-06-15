class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        N = len(profits)
        P = sorted(list(range(N)), key=lambda i:capital[i])
        pq = []
        for i in range(N):
            p,c = profits[P[i]], capital[P[i]]
            if c <= w:
                heappush(pq, -p)
            else: 
                while pq and k > 0 and w < c:
                    w += -heappop(pq)
                    k -= 1
                if k > 0 and w >= c:
                    heappush(pq, -p)
                else:
                    return w
        while k > 0 and pq:
            w += -heappop(pq)
            k -= 1
        return w