class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums) and nums[j] != nums[j-1]:
                res += j-i
                j += 1
            i = j
        return res + len(nums)