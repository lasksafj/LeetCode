class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def F(nums, k):
            s = sum(nums[:k])
            res = [-inf]*(len(nums))
            res[k-1] = s
            for i in range(k, len(nums)):
                s += nums[i]-nums[i-k]
                res[i] = max(res[i-1], s)
            return res
        lf = F(nums, firstLen)
        ls = F(nums, secondLen)
        rf = F(nums[::-1], firstLen)[::-1]
        rs = F(nums[::-1], secondLen)[::-1]
        res = 0
        for i in range(len(lf)-1):
            res = max(res, lf[i]+rs[i+1], ls[i]+rf[i+1])
        return res