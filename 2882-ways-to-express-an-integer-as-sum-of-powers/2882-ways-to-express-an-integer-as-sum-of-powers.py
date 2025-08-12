class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9+7
        ma = ceil(n**(1/x))
        @cache
        def dfs(n, i):
            if n == 0:
                return 1
            if i**x > n:
                return 0
            return (dfs(n, i+1) + dfs(n-i**x, i+1)) % MOD
        return dfs(n, 1)