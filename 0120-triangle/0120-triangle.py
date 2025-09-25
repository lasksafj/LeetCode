class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for row in triangle[::-1][1:]:
            ndp = [0] * len(row)
            for i in range(len(row)):
                ndp[i] = min(dp[i], dp[i+1]) + row[i]
            dp = ndp
        return dp[0]