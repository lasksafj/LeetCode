class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        for r in grid:
            for j in range(n):
                if r == [grid[i][j] for i in range(n)]:
                    res += 1
        return res