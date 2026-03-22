class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            N = len(mat)
            for i in range(N):
                for j in range(i, N):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for i in range(N):
                for j in range(N//2):
                    mat[i][j], mat[i][N-j-1]  = mat[i][N-j-1], mat[i][j]
        for _ in range(4):
            rotate(mat)
            for row in mat: print(row)
            if mat == target: return True
        return False