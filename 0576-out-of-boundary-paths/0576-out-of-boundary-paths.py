class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        res = 0
        dp = [[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1
        for k in range(maxMove):
            res = ( res + sum(dp[i][0] + dp[i][-1] for i in range(m)) + sum(dp[0] + dp[-1]) ) % MOD
            ndp = [[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    ndp[i][j] = ((dp[i][j-1] if j>0 else 0) + (dp[i][j+1] if j+1<n else 0) + (dp[i-1][j] if i>0 else 0) + (dp[i+1][j] if i+1<m else 0)) % MOD
            dp = ndp
        return res