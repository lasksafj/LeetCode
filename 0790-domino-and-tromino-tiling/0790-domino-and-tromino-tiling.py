class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        @cache
        def dfs(i, prev1, prev2):
            if i == n:
                return 1 if prev1 == 1 and prev2 == 1 else 0
            if i > n:
                return 0
            res = 0
            if prev1 == 1 and prev2 == 1:
                res = (res + dfs(i+1, 1, 1) + dfs(i+2, 1, 1) + dfs(i+2, 1, 0) + dfs(i+2, 0, 1)) % mod
            elif prev1 == 1 and prev2 == 0:
                res = (res + dfs(i+1, 1, 1) + dfs(i+1, 0, 1)) % mod
            elif prev1 == 0 and prev2 == 1:
                res = (res + dfs(i+1, 1, 1) + dfs(i+1, 1, 0)) % mod
            return res
        return dfs(0, 1, 1)