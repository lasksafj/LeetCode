class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        row = [[0]*(N+1) for _ in range(M)]
        col = [[0]*(M+1) for _ in range(N)]
        for i in range(M):
            for j in range(N):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[j][i+1] = col[j][i] + grid[i][j]
        res = 1
        for k in range(2, min(M,N)+1):
            for i in range(M-k+1):
                for j in range(N-k+1):
                    s = set()
                    diag1 = diag2 = 0
                    for ii in range(i, i+k):
                        s.add(row[ii][j+k] - row[ii][j])
                        diag1 += grid[ii][j + ii-i]
                    for jj in range(j, j+k):
                        s.add(col[jj][i+k] - col[jj][i])
                        diag2 += grid[i+k-1-(jj-j)][jj]
                    if len(s) == 1 and diag1 == diag2 == s.pop():
                        res = max(res, k)
        return res