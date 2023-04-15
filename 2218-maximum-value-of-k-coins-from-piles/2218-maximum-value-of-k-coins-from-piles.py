class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        if n == 1:
            return sum(piles[0][:k])
        dp,prev_dp = [0]*(k+1),[0]*(k+1)
        for i in range(n):
            for j in range(1,k+1):
                dp[j] = prev_dp[j]
                s = 0
                for l in range(1, min(j, len(piles[i]))+1):
                    s += piles[i][l-1]
                    dp[j] = max(dp[j], prev_dp[j-l] + s)
            prev_dp = dp[:]
        # print(dp)
        return dp[k]