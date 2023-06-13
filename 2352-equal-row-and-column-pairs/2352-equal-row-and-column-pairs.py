class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        m = Counter(tuple(r) for r in grid)
        for j in range(n):
            res += m[tuple([grid[i][j] for i in range(n)])]
        return res