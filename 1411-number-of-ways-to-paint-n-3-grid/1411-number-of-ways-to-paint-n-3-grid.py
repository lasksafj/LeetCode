class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i, last):
            if i == n:
                return 1
            res = 0
            for a in range(3):
                if a==last[0]: continue
                for b in range(3):
                    if b==a or b==last[1]: continue
                    for c in range(3):
                        if c==b or c==last[2]: continue
                        res += dfs(i+1, (a,b,c))
            return res % MOD
        return dfs(0, (-1,-1,-1))