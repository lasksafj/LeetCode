class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M,N = len(mat), len(mat[0])
        A = [[0]*(N+1) for _ in range(M+1)]
        for i in range(1, M+1):
            s = 0
            for j in range(1, N+1):
                s += mat[i-1][j-1]
                A[i][j] = A[i-1][j] + s
        res = 0
        k = min(M,N)
        for i in range(M+1):
            for j in range(N+1):
                while res <= k and i+res <= M and j+res <= N:
                    if A[i+res][j+res] - A[i+res][j] - A[i][res+j] + A[i][j] <= threshold:
                        res += 1
                    else:
                        break
        return res-1