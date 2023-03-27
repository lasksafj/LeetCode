class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        @cache
        def dfs(x,y):
            if x==m-1 and y==n-1:
                return grid[x][y]
            if x==m or y==n:
                return 99999
            return grid[x][y] + min(dfs(x+1,y), dfs(x,y+1) )
        return dfs(0,0)