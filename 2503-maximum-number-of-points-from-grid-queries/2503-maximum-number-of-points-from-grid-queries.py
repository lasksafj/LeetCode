class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m,n = len(grid), len(grid[0])
        pq = [[grid[0][0], 0, 0]]
        point = {}
        p = 0
        vis = [[0]*n for _ in range(m)]
        vis[0][0] = 1
        while pq:
            v,x,y = heapq.heappop(pq)
            for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx,ny = x+a,b+y
                if nx>=0 and ny>=0 and nx<m and ny<n and not vis[nx][ny]:
                    vis[nx][ny] = 1
                    nv = grid[nx][ny]
                    if nv < v:
                        nv = v
                    heapq.heappush(pq, [nv, nx, ny])
            p += 1
            point[v] = p
        
        pl = sorted([[a,b] for a,b in point.items()])
        res = []
        for q in queries:
            idx = bisect.bisect_left(pl, [q,0]) - 1
            if idx < 0:
                res.append(0)
            else:
                res.append(pl[idx][1])
        return res
                    