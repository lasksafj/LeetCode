class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        dp = [[inf]*N for _ in range(M)]
        res = -inf
        # dp[i][j] = min(dp[0][0]...dp[i][j])
        for i in range(M):
            for j in range(N):
                mi = inf
                if i > 0:
                    mi = min(mi, dp[i-1][j])
                if j > 0:
                    mi = min(mi, dp[i][j-1])
                if i > 0 or j > 0:
                    res = max(res, grid[i][j]-mi)
                dp[i][j] = min(mi, grid[i][j])
        
        return res