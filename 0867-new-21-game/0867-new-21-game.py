class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # dp[i]: prob for draw i points
        # dp[i] = sum(dp[j] * 1/maxPts) for j: i-maxPts-1 -> i-1
        dp = [0]*(n+1)
        dp[0] = 1
        s = 1 if k else 0
        for i in range(1, n+1):
            dp[i] = s/maxPts
            if i < k:
                s += dp[i]
            if 0 <= i-maxPts < k:
                s -= dp[i-maxPts]
        return sum(dp[k:])