class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i,v in enumerate(nums):
            dp[i] = max((dp[i-2] if i>=2 else 0) + v, dp[i-1] if i>=1 else 0)
        return dp[n-1]