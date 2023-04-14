class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            dp[j][j] = 1
            for i in range(j-1,-1,-1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # for r in dp:
        #     print(r)
        return dp[0][n-1]