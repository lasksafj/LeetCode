class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = (10**9+7)
        dp = [[0]*2 for _ in range(high+1)]
        dp[one][1] = 1
        dp[zero][0] = 1
        for i in range(1, high+1):
            if i - zero > 0:
                dp[i][0] = (dp[i-zero][0] + dp[i-zero][1]) % mod
            if i - one > 0:
                dp[i][1] = (dp[i-one][0] + dp[i-one][1]) % mod
        res = 0
        for i in range(low, high+1):
            res += (dp[i][0] + dp[i][1]) % mod
        return res % mod