class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        M,N = len(grid1),len(grid1[0])
        vis = set()
        dp = [[-1]*N for _ in range(M)]

        def dfs(i,j):
            if dp[i][j] > -1:
                return dp[i][j]
            if (i,j) in vis:
                return True
            vis.add((i,j))
            if grid1[i][j] == 0:
                dp[i][j] = 0
                return False
            
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N and grid2[ni][nj]:
                    if not dfs(ni,nj):
                        dp[i][j] = 0
                        return False

            dp[i][j] = 1
            return True
        
        res = 0
        for i in range(M):
            for j in range(N):
                if (i,j) not in vis and grid2[i][j]:
                    res += dfs(i,j)
        return res