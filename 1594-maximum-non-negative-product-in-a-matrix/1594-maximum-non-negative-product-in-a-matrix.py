class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        dp = [[[-inf]*2 for _ in range(N+1)] for _ in range(M+1)]
        dp[0][1][0] = 1
        for i in range(1, M+1):
            for j in range(1, N+1):
                g = grid[i-1][j-1]
                if g == 0:
                    dp[i][j][0] = dp[i][j][1] = 0
                    continue
                k = g&1
                dp[i][j][k] = max(dp[i-1][j][k^(g<0)], dp[i][j-1][k^(g<0)]) * abs(g)
                dp[i][j][k^1] = max(dp[i-1][j][k^1^(g<0)], dp[i][j-1][k^1^(g<0)]) * abs(g)
        return dp[-1][-1][0] % (10**9+7) if dp[-1][-1][0] > -inf else -1