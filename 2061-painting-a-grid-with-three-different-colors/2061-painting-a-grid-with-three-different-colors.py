class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i,j,prow):
            if i == n:
                return 1
            if j == m:
                return dfs(i+1, 0, prow)
            res = 0
            for c in range(3):
                if (j == 0 or c != prow[j-1]) and c != prow[j]:
                    res += dfs(i, j+1, prow[:j] + (c,) + prow[j+1:])
            return res % MOD
        return dfs(0,0,tuple([-1]*m))