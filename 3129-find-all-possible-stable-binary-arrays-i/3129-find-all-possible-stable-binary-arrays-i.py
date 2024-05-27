class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(zero, one, next_num):
            if zero == 0:
                return 1 if one <= limit and next_num == 1 else 0
            if one == 0:
                return 1 if zero <= limit and next_num == 0 else 0
            if next_num == 1:
                return (dfs(zero, one-1, 0) + dfs(zero, one-1, 1) \
                    - (dfs(zero, one-limit-1, 0) if one>limit else 0)) % MOD
            else:
                return (dfs(zero-1, one, 0) + dfs(zero-1, one, 1) \
                    - (dfs(zero-limit-1, one, 1) if zero>limit else 0)) % MOD
            
        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD