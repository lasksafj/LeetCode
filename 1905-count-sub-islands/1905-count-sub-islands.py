class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        M,N = len(grid1),len(grid1[0])
        vis = set()

        def dfs(i,j):
            vis.add((i,j))
            res = grid1[i][j]
            
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N and grid2[ni][nj] and (ni,nj) not in vis:
                    res &= dfs(ni,nj)
            return res
        
        res = 0
        for i in range(M):
            for j in range(N):
                if (i,j) not in vis and grid2[i][j]:
                    res += dfs(i,j)
        return res