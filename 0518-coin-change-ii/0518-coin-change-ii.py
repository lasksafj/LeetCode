class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for a in range(c, amount+1):
                dp[a] += dp[a-c]
        return dp[amount]