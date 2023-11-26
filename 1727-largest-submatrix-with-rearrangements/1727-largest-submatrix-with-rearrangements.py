class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        M,N = len(matrix),len(matrix[0])
        A = [[0]*N for _ in range(M)]
        for j in range(N):
            for i in range(M):
                if matrix[i][j] == 1:
                    A[i][j] = (A[i-1][j] if i>0 else 0) + 1
        res = 0
        for i in range(M):
            A[i].sort(reverse=True)
            # print(A[i])
            for k,n in enumerate(A[i]):
                res = max(res, n*(k+1))
        return res