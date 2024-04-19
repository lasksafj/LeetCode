class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M,N = len(grid),len(grid[0])
        vis = set()
        def dfs(i,j):
            if i<0 or i==M or j<0 or j==N or grid[i][j] == '0' or (i,j) in vis:
                return
            vis.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1' and (i,j) not in vis:
                    dfs(i,j)
                    res += 1
        return res