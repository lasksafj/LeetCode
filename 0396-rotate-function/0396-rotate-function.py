class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        N = len(nums)
        s = sum(nums)
        cur = 0
        for i in range(N):
            cur += nums[i]*i
        res = cur
        j = 0
        for i in range(N, 2*N):
            cur += nums[i%N]*i - nums[j]*j - s
            res = max(res, cur)
            j += 1
        return res