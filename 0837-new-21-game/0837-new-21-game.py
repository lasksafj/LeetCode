class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0]*(n+1)
        dp[0] = 1
        s = 0
        ls = 0
        for i in range(1,n+1):
            if i-1 < k:
                s += dp[i-1]
                ls += 1
            dp[i] = s/maxPts
            if (ls == maxPts or i > k) and i-maxPts >= 0 and s > 0:
                s -= dp[i-maxPts]
                ls -= 1
            
        return sum(dp[k:])