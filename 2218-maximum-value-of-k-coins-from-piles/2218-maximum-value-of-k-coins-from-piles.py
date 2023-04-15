class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        if n == 1:
            return sum(piles[0][:k])
        dp,prev_dp = [0]*(k+1),[0]*(k+1)
        s = 0
        for p in piles:
            for i in range(1, len(p)):
                p[i] += p[i - 1]
            s = min(s + len(p), k)
            for j in range(1,s+1):
                dp[j] = prev_dp[j]
                for l in range(1, min(j, len(p))+1):
                    dp[j] = max(dp[j], prev_dp[j-l] + p[l-1])
            prev_dp = dp[:]
        # print(dp)
        return dp[k]