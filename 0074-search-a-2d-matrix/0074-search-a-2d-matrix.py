class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l,r = 0,m*n-1
        while l <= r:
            mi = (l+r)//2
            i = mi//n
            j = mi%n
            if matrix[i][j] < target:
                l = mi+1
            elif matrix[i][j] > target:
                r = mi-1
            else:
                return True
        return False