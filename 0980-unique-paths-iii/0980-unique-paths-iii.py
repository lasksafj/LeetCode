class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def sol(x,y,k,m,n):
            if grid[x][y] == 2:
                if k == 0:
                    res[0] += 1
                return
            grid[x][y] = 1
            for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx,ny = x+a,y+b
                if nx>=0 and ny>=0 and nx<m and ny<n \
                    and (grid[nx][ny] == 0 or grid[nx][ny] == 2):
                    sol(nx,ny,k-1,m,n)
            grid[x][y] = 0
            
        m,n = len(grid),len(grid[0])
        res = [0]
        x,y,k = 0,0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x,y = i,j
                elif grid[i][j] == 0:
                    k += 1
        sol(x,y,k+1,m,n)
        return res[0]