class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        A = sorted(nums)
        return max(a+b for a,b in zip(A[:n//2], A[::-1][:n//2]))