class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M,N = len(matrix),len(matrix[0])
        first_row = first_col = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    if i and j:
                        matrix[0][j] = matrix[i][0] = 0
                    if i == 0:
                        first_row = 1
                    if j == 0:
                        first_col = 1
        for i in range(1, M):
            if matrix[i][0] == 0:
                matrix[i] = [0]*N
        for j in range(1, N):
            if matrix[0][j] == 0:
                for i in range(M):
                    matrix[i][j] = 0
        if first_row:
            matrix[0] = [0]*N
        if first_col:
            for i in range(M):
                matrix[i][0] = 0