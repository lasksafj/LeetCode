class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def sol(grid):
            s = sum(sum(row) for row in grid)
            if s&1: return False
            a = 0
            for row in grid:
                a += sum(row)
                if a == s//2: return True
            return False
        return sol(grid) or sol(list(zip(*grid)))