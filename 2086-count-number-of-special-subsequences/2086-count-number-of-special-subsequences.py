class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9+7
        dp = [0]*3
        for n in nums:
            dp[n] += (dp[n-1] if n else 0) + dp[n]
            if n == 0:
                dp[0] += 1
        return dp[2] % MOD