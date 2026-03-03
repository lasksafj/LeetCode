class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0]+nums
        N = len(nums)
        dp = [0]*N
        dp[1] = nums[1]
        for i in range(2, N):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]