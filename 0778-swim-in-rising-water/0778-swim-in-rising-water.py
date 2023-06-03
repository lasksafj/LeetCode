class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        pq = [(grid[0][0],0,0)]
        vis = [[1000000]*n for _ in range(m)]
        vis[0][0] = 0
        while pq:
            # print(pq)
            a,x,y = heappop(pq)
            for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if nx>=0 and ny>=0 and nx<m and ny<n and vis[nx][ny] > max(a, grid[nx][ny]):
                    b = max(a, grid[nx][ny])
                    vis[nx][ny] = b
                    heappush(pq, (b,nx,ny))
        return vis[m-1][n-1]