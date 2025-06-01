class Solution:
    def maxSum(self, nums: List[int]) -> int:
        A = [n for n in set(nums) if n > 0]
        if A: return sum(A)
        return max(nums)