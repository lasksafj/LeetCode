class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = sorted(nums)
        return max((A[-1]-1)*(A[-2]-1), (A[0]-1)*(A[1]-1))