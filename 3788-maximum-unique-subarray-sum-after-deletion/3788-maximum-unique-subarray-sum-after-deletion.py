class Solution:
    def maxSum(self, nums: List[int]) -> int:
        A = set(n for n in nums if n >= 0)
        return sum(A) if len(A) > 0 else max(nums)