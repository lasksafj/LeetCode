class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n0 = nums.count(0)
        if n0 == len(nums): return 0
        a = 0
        for n in nums:
            a ^= n
        return len(nums) if a else len(nums)-1