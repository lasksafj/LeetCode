class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i==M or j==N or grid[i][j]<=0:
                return 0
            grid[i][j] *= -1
            res = max(dfs(i+1,j),
                    dfs(i-1,j),
                    dfs(i,j+1),
                    dfs(i,j-1))
            grid[i][j] *= -1
            return res + grid[i][j]
        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i,j))
        return res