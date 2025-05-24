class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        @cache
        def dfs(i,j,di,dj,turn):
            way = [(di,dj,turn)]
            if turn:
                way.append((dj,-di,0))
            res = 0
            for dx,dy,t in way:
                ni,nj = i+dx,j+dy
                if 0<=ni<M and 0<=nj<N and grid[ni][nj] != grid[i][j] and grid[ni][nj] != 1:
                    if grid[i][j] != 1 or (grid[i][j] == 1 and grid[ni][nj] == 2):
                        res = max(res, dfs(ni,nj,dx,dy,t))
            return res + 1
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    res = max(res, 
                        dfs(i,j,1,1,1),
                        dfs(i,j,1,-1,1),
                        dfs(i,j,-1,-1,1),
                        dfs(i,j,-1,1,1)
                    )

        return res