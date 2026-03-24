class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        M,N = len(grid),len(grid[0])
        A = [[0]*N for _ in range(M)]
        A[0][0] = grid[0][0]
        for i in range(M):
            for j in range(N):
                if j:
                    A[i][j] = (A[i][j-1] * grid[i][j]) % 12345
                elif i:
                    A[i][j] = (A[i-1][N-1] * grid[i][j]) % 12345
        B = [[0]*N for _ in range(M)]
        B[-1][-1] = grid[-1][-1]
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if j < N-1:
                    B[i][j] = (B[i][j+1] * grid[i][j]) % 12345
                elif i < M-1:
                    B[i][j] = (B[i+1][0] * grid[i][j]) % 12345
        res = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                a = 1
                if j:
                    a = A[i][j-1]
                elif i:
                    a = A[i-1][N-1]
                b = 1
                if j < N-1:
                    b = B[i][j+1]
                elif i < M-1:
                    b = B[i+1][0]
                res[i][j] = a*b % 12345
        return res