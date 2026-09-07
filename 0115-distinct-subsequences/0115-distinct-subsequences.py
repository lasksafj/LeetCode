class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s = '#' + s
        t = '#' + t
        m,n = len(s),len(t)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(1, n):
            for i in range(1, m):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]