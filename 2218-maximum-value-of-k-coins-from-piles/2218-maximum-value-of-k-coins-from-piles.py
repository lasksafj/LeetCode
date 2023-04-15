class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        if n == 1:
            return sum(piles[0][:k])
        dp = [[0]*(k+1) for _ in range(n)]
        for i in range(n):
            for j in range(1,k+1):
                dp[i][j] = dp[i-1][j]
                s = 0
                for l in range(1, min(j, len(piles[i]))+1):
                    s += piles[i][l-1]
                    dp[i][j] = max(dp[i][j], dp[i-1][j-l] + s)
        # print(dp)
        return dp[n-1][k]