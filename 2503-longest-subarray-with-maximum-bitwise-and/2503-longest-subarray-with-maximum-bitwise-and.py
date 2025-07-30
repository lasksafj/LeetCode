class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma = max(nums)
        i = 0
        N = len(nums)
        res = 1
        while i < N:
            j = i+1
            while j < N and nums[i]==nums[j]:
                j += 1
            if nums[i] == ma:
                res = max(res, j-i)
            i = j
        return res