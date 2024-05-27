class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        # Solve 1:
        # @cache
        # def dfs(zero, one, next_num):
        #     if zero == 0:
        #         return 1 if one <= limit and next_num == 1 else 0
        #     if one == 0:
        #         return 1 if zero <= limit and next_num == 0 else 0
        #     if next_num == 1:
        #         return (dfs(zero, one-1, 0) + dfs(zero, one-1, 1) \
        #             - (dfs(zero, one-limit-1, 0) if one>limit else 0)) % MOD
        #     else:
        #         return (dfs(zero-1, one, 0) + dfs(zero-1, one, 1) \
        #             - (dfs(zero-limit-1, one, 1) if zero>limit else 0)) % MOD
        # return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
        
        # Solve 2:
        # dp[i][j][k]: number of stable arr that have i 0's, j 1's, ending with k(0,1)
        dp = [[[0, 0] for j in range(one+1)] for i in range(zero+1)]
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
        for i in range(1, zero+1):
            for j in range(1, one+1):
                dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
                if i > limit:
                    dp[i][j][0] -= dp[i-limit-1][j][1]
                dp[i][j][0] %= MOD
                dp[i][j][1] = dp[i][j-1][0] + dp[i][j-1][1]
                if j > limit:
                    dp[i][j][1] -= dp[i][j-limit-1][0]
                dp[i][j][1] %= MOD
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD