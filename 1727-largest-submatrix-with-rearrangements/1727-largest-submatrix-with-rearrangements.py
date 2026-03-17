class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        A = [0]*len(matrix[0])
        sl = SortedList(A)
        res = 0
        for row in matrix:
            for i,n in enumerate(row):
                p = A[i]
                A[i] = (A[i]+n) if n else 0
                sl.remove(p)
                sl.add(A[i])
            w = 1
            for n in sl[::-1]:
                res = max(res, n*w)
                w += 1
            
        return res