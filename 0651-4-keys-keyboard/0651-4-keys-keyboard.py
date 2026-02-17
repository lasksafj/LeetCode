class Solution:
    def maxA(self, n: int) -> int:
        dp = list(range(n+1))
        for i in range(n-2):
            for j in range(i+3, min(n, i+6)+1):
                dp[j] = max(dp[j], dp[i]*(j-i-1))
        return dp[-1]