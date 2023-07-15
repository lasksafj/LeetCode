class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        mod = 10**9+7
        dp = [[1]*n for _ in range(m)]
        cell = [(i,j) for i in range(m) for j in range(n)]
        cell.sort(key=lambda x:grid[x[0]][x[1]])
        for i,j in cell:
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] > grid[i][j]:
                    dp[ni][nj] = (dp[i][j] + dp[ni][nj]) % mod
        return sum(sum(dp[i]) for i in range(m)) % mod