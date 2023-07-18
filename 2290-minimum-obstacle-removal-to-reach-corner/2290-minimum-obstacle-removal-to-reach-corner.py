class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        vis = [[inf]*n for _ in range(m)]
        pq = [(grid[0][0],0,0)]
        while pq:
            # print(pq)
            k,x,y = heappop(pq)
            for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0 <= nx < m and 0 <= ny < n:
                    d = grid[nx][ny]
                    if k+d < vis[nx][ny]:
                        vis[nx][ny] = k+d
                        heappush(pq, (k+d,nx,ny))
        return vis[m-1][n-1]