class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for n in stones:
            heappush(pq, -n)
        while len(pq) > 1:
            a = -heappop(pq)
            b = -heappop(pq)
            if a == b:
                continue
            heappush(pq, -abs(a-b))
        return -pq[0] if pq else 0