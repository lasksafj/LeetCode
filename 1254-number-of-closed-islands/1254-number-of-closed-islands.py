class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        vis = set()
        def dfs(x,y):
            if x < 0 or x == m or y < 0 or y == n:
                return False
            if grid[x][y] == 1:
                return True
            if (x,y) in vis:
                return True
            vis.add((x,y))
            d1 = dfs(x+1,y) 
            d2 = dfs(x-1,y) 
            d3 = dfs(x,y+1) 
            d4 = dfs(x,y-1)
            return d1 and d2 and d3 and d4
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in vis:
                    res += dfs(i,j)
        return res