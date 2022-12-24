class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0]*4
        dp[0], dp[1], dp[2], dp[3] = 0,1,2,5
        for i in range(4, n+1):
            dp[i%4] = (2 * dp[(i-1)%4] + dp[(i-3)%4]) % 1000000007
        return dp[n%4] % 1000000007