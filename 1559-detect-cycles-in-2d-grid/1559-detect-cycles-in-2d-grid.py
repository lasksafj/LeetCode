class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        M,N = len(grid),len(grid[0])
        vis = set()
        def dfs(i,j,pi,pj):
            if (i,j) in vis:
                return True
            vis.add((i,j))
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N and (ni!=pi or nj!=pj) and grid[i][j]==grid[ni][nj] and dfs(ni,nj,i,j):
                    return True
            return False
        for i in range(M):
            for j in range(N):
                if (i,j) not in vis and dfs(i,j,-1,-1):
                    return True
        return False