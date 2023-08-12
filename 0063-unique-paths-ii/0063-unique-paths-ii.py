class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M,N = len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[M-1][N-1] == 1:
            return 0
        dp = defaultdict(int)
        dp[0,0] = 1
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j] != 1 and (i != 0 or j != 0):
                    dp[i,j] = (dp[i-1,j] if i>0 else 0) + (dp[i,j-1] if j>0 else 0)
        return dp[M-1,N-1]