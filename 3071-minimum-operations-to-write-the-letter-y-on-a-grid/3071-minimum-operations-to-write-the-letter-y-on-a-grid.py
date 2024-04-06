class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        N = len(grid)
        def sol(a,b):
            res = 0
            for i in range(N):
                for j in range(N):
                    if (j < N//2 and i == j) or (j>N//2 and N-i-1 == j) or (j==N//2 and i>=N//2):
                        res += grid[i][j] != a
                    else:
                        res += grid[i][j] != b
            return res
        return min(sol(0,1), sol(0,2), sol(1,2), sol(1,0), sol(2,0), sol(2,1))