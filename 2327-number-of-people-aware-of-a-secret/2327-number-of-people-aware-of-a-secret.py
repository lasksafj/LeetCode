class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*n
        dp[0] = 1
        mod = 10**9+7
        for i in range(n):
            for j in range(i+delay, min(n, i+forget)):
                dp[j] = (dp[j] + dp[i]) % mod
        # print(dp)
        return sum(dp[-forget:]) % mod