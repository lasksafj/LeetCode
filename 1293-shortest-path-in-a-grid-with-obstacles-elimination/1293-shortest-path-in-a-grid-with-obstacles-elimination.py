class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        m,n = len(grid), len(grid[0])
        if (m==1 and n==1) or m+n-1 <= k:
            return m+n-2
            
        q = deque([[k,0,0]])
        vis = [[[0]*n for _ in range(m)] for _ in range(k+1)]
        res = 0
        while q:
            s = len(q)
            res += 1
            for i in range(s):
                curk,x,y = q[0]
                q.popleft()
                for a,b in directions:
                    nx = x+a
                    ny = y+b
                    if nx >= 0 and ny >= 0 and nx < m and ny < n:
                        nk = curk - grid[nx][ny]
                        if nk >= 0 and not vis[nk][nx][ny]:
                            q.append([nk,nx,ny])
                            vis[nk][nx][ny] = 1
                            if nx == m-1 and ny == n-1:
                                return res
        # print(vis)
        return -1