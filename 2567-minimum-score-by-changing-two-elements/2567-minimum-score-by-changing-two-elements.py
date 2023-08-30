class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        A = sorted(nums)
        return min(A[-2] - A[1], A[-1] - A[2], A[-3] - A[0])