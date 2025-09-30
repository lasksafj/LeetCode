class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i,n in enumerate(nums):
            res += comb(N-1,i)*n
        return res % 10