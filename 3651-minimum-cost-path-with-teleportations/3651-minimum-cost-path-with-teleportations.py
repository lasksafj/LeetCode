class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        M,N = len(grid),len(grid[0])
        A = [[i,j,grid[i][j]] for i in range(M) for j in range(N)]
        A.sort(key=lambda e:-e[2])
        mp = {}
        mp[A[-1][0],A[-1][1]] = len(A)-1
        for i in range(len(A)-2, -1, -1):
            if A[i][2] == A[i+1][2]:
                mp[A[i][0], A[i][1]] = mp[A[i+1][0], A[i+1][1]]
            else:
                mp[A[i][0], A[i][1]] = i
        min_arr = [inf]*len(A)
        dp = [[[inf] * (k+1) for _ in range(N)] for _ in range(M)]
        for d in range(k+1):
            for i in range(M):
                for j in range(N):
                    if (i,j) == (0,0):
                        dp[i][j][d] = 0
                    else:
                        dp[i][j][d] = min(min(dp[i-1][j][d], dp[i][j-1][d]) + grid[i][j], min_arr[mp[i,j]] )
            i,j = A[0][0], A[0][1]
            min_arr[0] = dp[i][j][d]
            for idx in range(1, len(A)):
                i,j,_ = A[idx]
                min_arr[idx] = min(dp[i][j][d], min_arr[idx-1])
        return dp[M-1][N-1][k]