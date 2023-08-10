class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        pq = nums[:]
        heapify(pq)
        while k > 0:
            heappush(pq, heappop(pq) + 1)
            k -= 1
        res = 1
        mod = 10**9+7
        for n in pq:
            res = (res * n) % mod
        return res