class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        N = len(values)
        dp = [[inf]*N for _ in range(N)]
        for j in range(N):
            dp[j-1][j] = 0
            for i in range(j-2,-1,-1):
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i]*values[k]*values[j])
        return dp[0][N-1]