class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        pq = nums[:]
        heapify(pq)
        nums.sort()
        res = 0
        for v in nums:
            while pq and pq[0] <= v:
                heappop(pq)
            if pq:
                heappop(pq)
                res += 1
        return res