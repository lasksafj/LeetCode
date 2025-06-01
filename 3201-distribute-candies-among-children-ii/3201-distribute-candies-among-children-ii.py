class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # dp[i][k]: no_ways to distribute i childrens k candies
        # dp = [0]*(n+1)
        # pre = [1]*(n+1)
        # for i in range(1, 4):
        #     npre = [0] * (n+1)
        #     for k in range(n+1):
        #         dp[k] = pre[k] - (pre[k-limit-1] if k > limit else 0)
        #         npre[k] = (npre[k-1] if k else 0) + dp[k]
        #     pre = npre
        # return dp[n]

        # Total no ways to distribute n to 3 childrens: comb(n+2, 2)
        # At least one child receives more than limit candies: comb(n+2-(limit+1), 2) * 3
        # At least two children receive more than limit candies: comb(n+2 - 2*(limit+1), 2) * 3
        # All three children receive more than limit candies: comb(n+2 - 3*(limit+1, 2))

        total = comb(n+2, 2) 
        at_least_1 = comb(n+2-(limit+1), 2) * 3  if n+2-(limit+1) >= 0 else 0
        at_least_2 = comb(n+2 - 2*(limit+1), 2) * 3 if n+2 - 2*(limit+1) >= 0 else 0
        at_least_3 = comb(n+2 - 3*(limit+1), 2) if n+2 - 3*(limit+1) >= 0 else 0
        return total - at_least_1 + at_least_2 - at_least_3