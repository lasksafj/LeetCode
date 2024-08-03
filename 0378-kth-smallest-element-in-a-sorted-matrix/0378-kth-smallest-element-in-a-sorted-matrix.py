class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(mi):
            res = 0
            for row in matrix:
                res += bisect_right(row, mi)
            # print(mi, res)
            return res < k
            
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                l = mi+1
            else:
                r = mi-1
        return l