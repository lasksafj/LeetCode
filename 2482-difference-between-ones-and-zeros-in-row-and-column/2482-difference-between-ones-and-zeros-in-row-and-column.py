class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        M,N = len(grid),len(grid[0])
        onesRow = [0]*M
        onesCol = [0]*N
        for i in range(M):
            for j in range(N):
                onesRow[i] += grid[i][j]
                onesCol[j] += grid[i][j]
        res = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                res[i][j] = 2*onesRow[i] + 2*onesCol[j] - M - N
        return res