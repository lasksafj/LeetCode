class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        a = 0
        for i,n in enumerate(nums):
            a += i*n
        res = a
        l = 0
        r = s
        for n in nums:
            r -= n
            a = a-r-l+n*(len(nums)-1)
            l += n
            res = max(res, a)
        return res