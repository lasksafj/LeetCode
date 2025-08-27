class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        @cache
        def dfs(x,y,dx,dy,turn):
            D = [[dx,dy,turn]]
            if turn:
                D += [[dy,-dx,0]]
            res = 0
            for ndx,ndy,t in D:
                nx,ny = x+ndx,y+ndy
                if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] != grid[x][y] and grid[nx][ny] != 1:
                    if grid[x][y] != 1 or (grid[x][y] == 1 and grid[nx][ny] == 2):
                        res = max(res, dfs(nx,ny,ndx,ndy,t))
            return res+1
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    for dx,dy in [[1,1],[-1,1],[-1,-1],[1,-1]]:
                        res = max(res, dfs(i,j,dx,dy,1))
        return res