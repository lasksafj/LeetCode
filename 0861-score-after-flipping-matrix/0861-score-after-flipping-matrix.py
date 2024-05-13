class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        
        for i in range(M):
            n = 0
            for j in grid[i]:
                n = (n<<1) + j
            if n < n^((1<<N)-1):
                for j in range(N):
                    grid[i][j] ^= 1
        
        for j in range(N):
            if sum(grid[i][j] for i in range(M)) < M/2:
                for i in range(M):
                    grid[i][j] ^= 1
        
        res = 0
        for row in grid:
            n = 0
            for j in row:
                n = (n<<1) + j
            res += n
        return res