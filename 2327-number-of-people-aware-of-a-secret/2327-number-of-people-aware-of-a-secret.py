class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*n #prefix sum
        s = 0
        dp[0] = 1
        mod = 10**9+7
        for i in range(1,n):
            s = (s + dp[i-delay] - dp[i-forget]) % mod
            dp[i] = s
        return sum(dp[-forget:]) % mod