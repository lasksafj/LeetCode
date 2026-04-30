class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        M,N = len(grid),len(grid[0])
        dp = [[[-inf]*(k+1) for _ in range(N+1)] for _ in range(M+1)]
        dp[0][1][0] = dp[1][0][0] = 0
        for i in range(1, M+1):
            for j in range(1, N+1):
                v = grid[i-1][j-1]
                score = v
                cost = min(v, 1)
                for kk in range(cost, k+1):
                    dp[i][j][kk] = max(
                        dp[i][j][kk], 
                        dp[i-1][j][kk-cost] + score, 
                        dp[i][j-1][kk-cost] + score
                    )
        res = max(dp[-1][-1])
        return res if res > -inf else -1