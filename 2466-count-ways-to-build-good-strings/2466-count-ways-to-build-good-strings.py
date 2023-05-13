class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1000000007
        dp = [0] * (high+1)
        dp[0] = 1
        for i in range(1, high+1):
            dp[i] = (dp[i-zero] + dp[i-one]) % MOD
        return sum(dp[low:]) % MOD