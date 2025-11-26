class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M,N = len(grid), len(grid[0])
        dp = [[[-1]*k for _ in range(N)] for _ in range(M)]
        def dfs(i,j,m):
            if i < 0 or j < 0 or i == M or j == N:
                return 0
            m = (m + grid[i][j]) % k
            if dp[i][j][m] > -1:
                return dp[i][j][m]
            if (i,j) == (M-1,N-1):
                dp[i][j][m] = 1 if m == 0 else 0
            else:
                dp[i][j][m] = dfs(i+1,j, m) + dfs(i,j+1, m)
            return dp[i][j][m]
        return dfs(0,0,0) % (10**9+7)