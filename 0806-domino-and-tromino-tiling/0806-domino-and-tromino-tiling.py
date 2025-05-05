class Solution:
    def numTilings(self, n: int) -> int:
        # dp[n]=dp[n-1]+dp[n-2]+ 2*(dp[n-3]+...+d[0])
        # = dp[n-1]+dp[n-2]+dp[n-3]+dp[n-3]+2*(dp[n-4]+...+d[0])
        # = dp[n-1]+dp[n-3]+(dp[n-2]+dp[n-3]+2*(dp[n-4]+...+d[0]))
        # = dp[n-1]+dp[n-3]+dp[n-1]
        # = 2*dp[n-1]+dp[n-3]
        MOD = 10**9+7
        dp = [1, 2, 5] + [0] * (n-3)
        for i in range(3, n):
            dp[i] = 2*dp[i-1] + dp[i-3]
        return dp[n-1] % MOD