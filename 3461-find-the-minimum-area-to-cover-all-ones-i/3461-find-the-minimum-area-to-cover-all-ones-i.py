class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        a,c = inf,inf
        b,d = -inf,-inf
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    a = min(a, j)
                    b = max(b, j)
                    c = min(c, i)
                    d = max(d, i)
        return (b-a+1) * (d-c+1)