class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        m,n = len(grid),len(grid[0])
        i,j = m-1,0
        while i >= 0:
            while j < n and grid[i][j] >= 0:
                j += 1
            if j > 0:
                j -= 1
                res += n-j-1
            else:
                res += n
            i -= 1
        return res