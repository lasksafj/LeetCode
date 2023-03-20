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
            if (a,b) not in [(x+1,y+2),(x+2,y+1),(x-1,y-2),(x-2,y-1),(x-1,y+2),(x-2,y+1),(x+1,y-2),(x+2,y-1)]:
                return False
            x,y = a,b
        return True
            