class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(mi):
            res = 0
            i = len(matrix[0])-1
            for row in matrix:
                while i >= 0 and row[i] > mi:
                    i -= 1
                res += i+1
            return res >= k
            
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l