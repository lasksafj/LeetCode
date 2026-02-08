class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        dp = [[[-inf]*2 for _ in range(k+1)] for _ in range(N+1)]
        for j in range(k+1):
            dp[0][j][0] = 0
        for i in range(1, N+1):
            p = prices[i-1]
            for j in range(k+1):
                if j:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - p)
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + p)
        return dp[-1][k][0]