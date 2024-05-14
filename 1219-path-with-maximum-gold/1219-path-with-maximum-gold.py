class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        vis = [[False]*N for _ in range(M)]
        def dfs(i,j):
            if i<0 or j<0 or i==M or j==N or vis[i][j] or grid[i][j]==0:
                return 0
            vis[i][j] = True
            res = max(dfs(i+1,j),
                    dfs(i-1,j),
                    dfs(i,j+1),
                    dfs(i,j-1))
            vis[i][j] = False
            return res + grid[i][j]
        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i,j))
        return res