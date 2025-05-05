class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        dp = [[[0]*2 for _ in range(2)] for _ in range(n+2)]
        dp[1][1][1] = 1
        for i in range(2, n+2):
            dp[i][1][1] = dp[i-1][1][1] + dp[i-1][0][1] + dp[i-1][1][0] + dp[i-2][1][1]
            dp[i][0][1] = dp[i-2][1][1] + dp[i-1][1][0]
            dp[i][1][0] = dp[i-2][1][1] + dp[i-1][0][1]
        return dp[-1][1][1] % MOD