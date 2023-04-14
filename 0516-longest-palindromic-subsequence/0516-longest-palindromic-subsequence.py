class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp,pre_dp = [0]*n,[0]*n
        for j in range(n):
            dp[j] = 1
            for i in range(j-1,-1,-1):
                if s[i] == s[j]:
                    dp[i] = pre_dp[i+1] + 2
                else:
                    dp[i] = max(dp[i+1], pre_dp[i])
            pre_dp = dp[:]
        # for r in dp:
        #     print(r)
        return dp[0]