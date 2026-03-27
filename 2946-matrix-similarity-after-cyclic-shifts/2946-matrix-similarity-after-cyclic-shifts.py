class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        N = len(mat[0])
        A = []
        k %= N
        if k == 0: return True
        for i,row in enumerate(mat):
            if i&1:
                A.append(row[-k:] + row[k:])
            else:
                A.append(row[k:] + row[:k])
        return mat == A