class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        A = sorted(nums)
        a,b,c = A[-3:]
        e,f = A[:2]
        return max(a*b*c, e*f*c)