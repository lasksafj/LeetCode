class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        for z in range(min(limit, zero) + 1):
            dp[z][0][0] = 1
        for o in range(min(limit, one) + 1):
            dp[0][o][1] = 1
        for z in range(1, zero+1):
            for o in range(1, one+1):
                dp[z][o][0] = sum(dp[z-1][o])
                if z > limit:
                    dp[z][o][0] -= dp[z-limit-1][o][1]
                dp[z][o][1] = sum(dp[z][o-1])
                if o > limit:
                    dp[z][o][1] -= dp[z][o-limit-1][0]
        return (dp[z][o][0] + dp[z][o][1]) % (10**9+7)