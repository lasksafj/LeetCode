class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        res = 0
        j = N-1
        for i in range(M):
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            res += N-j-1
        return res