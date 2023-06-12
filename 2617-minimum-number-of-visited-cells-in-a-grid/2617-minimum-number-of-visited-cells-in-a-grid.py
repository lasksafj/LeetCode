class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if m==1 and n==1:
            return 1
        pq_r = [[] for _ in range(m)]
        pq_c = [[] for _ in range(n)]
        pq_r[0] = [[1, 0]]
        pq_c[0] = [[1, 0]]
        c = inf
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                c = inf
                while pq_r[i] and pq_r[i][0][1] + grid[i][pq_r[i][0][1]] < j:
                    heappop(pq_r[i])
                while pq_c[j] and pq_c[j][0][1] + grid[pq_c[j][0][1]][j] < i:
                    heappop(pq_c[j])
                a = pq_r[i][0][0] if pq_r[i] else inf
                b = pq_c[j][0][0] if pq_c[j] else inf
                c = min(a,b)+1
                # print(i,j,a,b,c)
                if c < inf:
                    heappush(pq_r[i], [c, j])
                    heappush(pq_c[j], [c, i])

        return c if c < inf else -1