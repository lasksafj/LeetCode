class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        c = [0]*len(mat[0])
        for j,col in enumerate(zip(*mat)):
            if col.count(1) == 1:
                c[j] = 1
        for row in mat:
            if row.count(1) == 1:
                res += c[row.index(1)]
        
        return res