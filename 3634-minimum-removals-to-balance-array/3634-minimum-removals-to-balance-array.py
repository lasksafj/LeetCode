class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        res = N
        j = 0
        for i,n in enumerate(nums):
            while j < N and nums[j] <= n*k:
                j += 1
            res = min(res, N-(j-i))
        return res