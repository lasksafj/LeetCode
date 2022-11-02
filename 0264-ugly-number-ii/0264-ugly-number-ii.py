class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        n2,n3,n5 = 0,0,0
        for i in range(1, n):
            dp[i] = min(dp[n2]*2, dp[n3]*3, dp[n5]*5)
            if dp[i] == dp[n2]*2:
                n2 += 1
            if dp[i] == dp[n3]*3:
                n3 += 1
            if dp[i] == dp[n5]*5:
                n5 += 1
        return dp[n-1]