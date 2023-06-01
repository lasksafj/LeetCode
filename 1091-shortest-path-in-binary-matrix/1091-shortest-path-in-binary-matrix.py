class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1
        if m==1 and n==1:
            return 1
        vis = set()
        vis.add((0,0))
        q = deque([(0,0)])
        res = 1
        while q:
            res += 1
            for _ in range(len(q)):
                x,y = q.popleft()
                for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1],[x+1,y+1],[x-1,y-1],[x+1,y-1],[x-1,y+1]]:
                    if nx>=0 and ny>=0 and nx<m and ny<n and (nx,ny) not in vis and grid[nx][ny]==0:
                        if nx==m-1 and ny==n-1:
                            return res
                        q.append((nx,ny))
                        vis.add((nx,ny))
        return -1
                    