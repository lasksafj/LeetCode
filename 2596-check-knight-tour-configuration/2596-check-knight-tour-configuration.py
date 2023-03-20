class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = [() for _ in range(n*n)]
        for i in range(n):
            for j in range(n):
                m[grid[i][j]] = (i,j)
        if m[0] != (0,0):
            return False
        x,y = 0,0
        for i in range(1,n*n):
            a,b = m[i]
            if not ((abs(a-x) == 1 and abs(b-y) == 2) or (abs(a-x) == 2 and abs(b-y) == 1)):
                return False
            x,y = a,b
        return True
            