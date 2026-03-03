class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M,N = len(grid),len(grid[0])
        def dfs(i,j):
            if (i,j) in vis or grid[i][j] == '0': return
            vis.add((i,j))
            for ni,nj in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N:
                    dfs(ni,nj)
        vis = set()
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1' and (i,j) not in vis:
                    res += 1
                    dfs(i,j)
        return res