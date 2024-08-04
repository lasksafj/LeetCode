class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        res = 1
        j = 0
        cur = 0
        for i in range(N):
            while cur & nums[i] != 0:
                cur ^= nums[j]
                j += 1
            cur ^= nums[i]
            res = max(res, i-j+1)
        return res