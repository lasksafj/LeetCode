class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s = sum(sum(row) for row in grid)
        def f(mat):
            cur = 0
            for row in mat:
                cur += sum(row)
                if cur == s-cur:
                    return True
            return False
        return f(grid) or f(zip(*grid))