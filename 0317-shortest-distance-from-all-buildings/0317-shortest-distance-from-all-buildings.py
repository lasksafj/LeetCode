class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        dist = [[[0]*2 for _ in range(N)] for _ in range(M)]
        no1 = sum(row.count(1) for row in grid)
        def bfs(i,j):
            q = deque([[i,j]])
            d = 0
            vis = [[0]*N for _ in range(M)]
            vis[i][j] = 1
            res = 0
            while q:
                d += 1
                for _ in range(len(q)):
                    i,j = q.popleft()
                    for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                        if 0<=ni<M and 0<=nj<N and vis[ni][nj] == 0 and grid[ni][nj] == 0:
                            vis[ni][nj] = 1
                            q.append([ni,nj])
                            dist[ni][nj][0] += d
                            dist[ni][nj][1] += 1

        res = inf
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    bfs(i,j)
        for i in range(M):
            for j in range(N):
                if dist[i][j][1] == no1:
                    res = min(res, dist[i][j][0])
        return res if res < inf else -1