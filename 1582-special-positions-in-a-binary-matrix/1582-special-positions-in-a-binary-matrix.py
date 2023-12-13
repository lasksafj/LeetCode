class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = [0]*len(mat)
        col = [0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    row[i] += 1
                    col[j] += 1
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and row[i]+col[j] == 2:
                    res += 1
        return res