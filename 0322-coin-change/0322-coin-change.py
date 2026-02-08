class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf]*amount
        for c in coins:
            for a in range(c, amount+1):
                dp[a] = min(dp[a], dp[a-c] + 1)
        return dp[amount] if dp[amount] < inf else -1