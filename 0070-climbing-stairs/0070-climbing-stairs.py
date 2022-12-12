class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*3
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3]
        return dp[n%3]