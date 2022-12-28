class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        s = sum(piles)
        piles = [-p for p in piles]
        heapq.heapify(piles)
        res = 0
        while k > 0:
            a = -heapq.heappop(piles)
            b = a - a//2
            heapq.heappush(piles, -b)
            s -= a//2
            k -= 1
        return s