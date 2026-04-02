class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        M,N = len(coins),len(coins[0])
        dp = [[[-inf]*3 for _ in range(N+1)] for _ in range(M+1)]
        dp[1][1][0] = coins[0][0]
        dp[1][1][1] = 0
        for i in range(1, M+1):
            for j in range(1, N+1):
                if (i,j) == (1,1): continue
                c = coins[i-1][j-1]
                for k in range(3):
                    dp[i][j][k] = max(
                        max(dp[i-1][j][k-1], dp[i][j-1][k-1]) if k else -inf, 
                        max(dp[i-1][j][k], dp[i][j-1][k]) + c
                    )
        return max(dp[-1][-1])