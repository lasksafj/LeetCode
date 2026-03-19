class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        M,N = len(grid),len(grid[0])
        rowx = [0]*N
        rowy = [0]*N
        res = 0
        for i in range(M):
            x = y = 0
            for j in range(N):
                x += grid[i][j] == 'X'
                y += grid[i][j] == 'Y'
                rowx[j] += x
                rowy[j] += y
                if rowx[j]:
                    res += rowx[j] == rowy[j]
        return res