class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        res = 0
        dp = grid[0].copy()
        for i in range(1,M):
            ndp = grid[i].copy()
            for j in range(1,N-1):
                if grid[i][j]:
                    ndp[j] = min(dp[j-1:j+2]) + 1
                    res += ndp[j] - 1
            # print(dp,ndp)
            dp = ndp

        # print(res)
        dp = grid[M-1].copy()
        for i in range(M-2,-1,-1):
            ndp = grid[i].copy()
            for j in range(1,N-1):
                if grid[i][j]:
                    ndp[j] = min(dp[j-1:j+2]) + 1
                    res += ndp[j] - 1
            dp = ndp
        return res