class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        M,N = len(grid),len(grid[0])
        A = [[0]*(N+1) for _ in range(M+1)]
        res = 0
        for i in range(1,M+1):
            for j in range(1,N+1):
                A[i][j] = A[i][j-1] + A[i-1][j] - A[i-1][j-1] + grid[i-1][j-1]
                if A[i][j] <= k:
                    res += 1
        return res