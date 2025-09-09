class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        pre = [0] * (n+1)
        pre[1] = 1
        for i in range(2,n+1):
            dp[i] = pre[i-delay] - pre[i-forget]
            pre[i] = pre[i-1] + dp[i]
        return sum(dp[-forget:]) % (10**9+7)