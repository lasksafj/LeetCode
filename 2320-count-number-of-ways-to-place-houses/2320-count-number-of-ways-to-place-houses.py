class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9+7
        @cache
        def dfs(i, prev):
            if i == n:
                return 1
            res = dfs(i+1, 0)
            if prev == 0:
                res = (res + dfs(i+1, 1)) % mod
            return res
        a = dfs(0,0)
        return a*a % mod