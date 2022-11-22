class Solution:
    def numSquares(self, n: int) -> int:
        pqn = [i*i for i in range(1, int(sqrt(n)+1))]
        dp = [10000]*(n+1)
        for i in pqn:
            dp[i] = 1
        for i in range(1, n+1):
            dp[i] = min([dp[i]] + [dp[k] + dp[i-k] for k in pqn if k < i])
        
        return dp[n]