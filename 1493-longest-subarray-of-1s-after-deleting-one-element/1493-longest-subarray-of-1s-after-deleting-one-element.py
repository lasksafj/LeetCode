class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums)-1
        res,j = 0,0
        k = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k += 1
                while j < i and k > 1:
                    if nums[j] == 0:
                        k -= 1
                    j += 1
            res = max(res, i-j+1-k)
        return res