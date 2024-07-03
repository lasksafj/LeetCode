class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = inf
        for i in range(4):
            res = min(res, nums[-(i+1)] - nums[3-i])
        return res