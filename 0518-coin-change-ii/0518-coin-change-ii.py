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
            res = 0
            while a >= 0:
                res += dfs(i+1,a)
                a -= coins[i]
            return res
        return dfs(0,amount)