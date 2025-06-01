class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # dp[i][k]: no_ways to distribute i childrens k candies
        dp = [0]*(n+1)
        pre = [1]*(n+1)
        for i in range(1, 4):
            npre = [0] * (n+1)
            for k in range(n+1):
                dp[k] = pre[k] - (pre[k-limit-1] if k > limit else 0)
                npre[k] = (npre[k-1] if k else 0) + dp[k]
            pre = npre
        return dp[n]