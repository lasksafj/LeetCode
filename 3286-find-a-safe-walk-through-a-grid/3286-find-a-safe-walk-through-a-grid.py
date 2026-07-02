class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        M,N = len(grid),len(grid[0])
        q = deque([[0,0]])
        cost = [[inf]*N for _ in range(M)]
        cost[0][0] = grid[0][0]
        while q:
            i,j = q.popleft()
            if (i,j) == (M-1,N-1):
                return True
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N:
                    ncost = cost[i][j] + grid[ni][nj]
                    if ncost < health and ncost < cost[ni][nj]:
                        cost[ni][nj] = cost[i][j] + grid[ni][nj]
                        q.append([ni,nj])
        return False