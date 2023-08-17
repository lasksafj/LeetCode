class Solution:
    def minInsertions(self, s: str) -> int:
#         longest palindromic subsequence in s
        dp = [[1]*len(s) for _ in range(len(s))]
        for l in range(2, len(s)+1):
            for i in range(len(s)-l+1):
                j = i+l-1
                if j-i >= 2:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1], dp[i+1][j-1] + (s[i] == s[j])*2)
                else:
                    dp[i][j] = 2 if s[i] == s[j] else 1
        return len(s) - dp[0][len(s)-1]