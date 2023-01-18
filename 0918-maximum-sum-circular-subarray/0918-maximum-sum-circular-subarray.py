class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ma,mi = 0,0
        maxs,mins = -inf,inf
        for n in nums:
            ma += n
            maxs = max(maxs, ma)
            if ma < 0:
                ma = 0
            mi += n
            mins = min(mins, mi)
            if mi > 0:
                mi = 0
        s = sum(nums)
        return max(maxs, s - mins if s > mins else maxs)
            