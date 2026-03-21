class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        A = [grid[a][y:y+k] for a in range(x, x+k)]
        for i in range(x,x+k):
            grid[i][y:y+k] = A.pop()
        return grid