class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        M,N = len(grid),len(grid[0])
        onesRow = [0]*M
        onesCol = [0]*N
        zerosRow = [0]*M
        zerosCol = [0]*N
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    onesRow[i] += 1
                    onesCol[j] += 1
                else:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
        res = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                res[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        return res