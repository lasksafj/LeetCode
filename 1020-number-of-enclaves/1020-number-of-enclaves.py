class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        vis = set()
        q = deque()
        res = 0
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and grid[i][j]==1:
                    q.append((i,j))
                    res += 1
                    vis.add((i,j))
        while q:
            x,y = q.popleft()
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx,ny = x+dx,y+dy
                if nx>=0 and ny>=0 and nx<m and ny<n and grid[nx][ny]==1 and (nx,ny) not in vis:
                    vis.add((nx,ny))
                    q.append((nx,ny))
                    res += 1
        return sum(sum(r) for r in grid) - res