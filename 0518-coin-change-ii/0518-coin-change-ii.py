class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = [0]*(amount+1)
        # dp[0] = 1
        # for a in range(1, amount+1):
        #     for c in coins:
        #         if a-c >= 0:
        #             dp[a] += dp[a-c] + 1
        # return dp[amount]
        
        @cache
        def dfs(i,a):
            if a == 0:
                return 1
            if i == len(coins):
                return 0
            if a < coins[i]:
                return dfs(i+1,a)
            return dfs(i+1,a) + dfs(i, a-coins[i])
        return dfs(0,amount)