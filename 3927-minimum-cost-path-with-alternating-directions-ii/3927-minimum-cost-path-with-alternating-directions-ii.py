class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j] if i else inf, dp[i][j-1] if j else inf) + (i+1)*(j+1) + waitCost[i][j]
        return dp[-1][-1] - waitCost[-1][-1]