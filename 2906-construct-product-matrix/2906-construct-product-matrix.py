class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        M,N = len(grid),len(grid[0])
        A = [[0]*N for _ in range(M)]
        a = 1
        for i in range(M):
            for j in range(N):
                A[i][j] = a
                a = a*grid[i][j] % 12345
        B = [[0]*N for _ in range(M)]
        b = 1
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                B[i][j] = b
                b = b*grid[i][j] % 12345
        res = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                res[i][j] = A[i][j] * B[i][j] % 12345
        return res