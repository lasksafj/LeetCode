class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        @cache
        def sol(i, k):
            if k == 0 and i <= n:
                return 1
            if i >= n:
                return 0
            res = sol(i+1, k)
            if s[i] in '2357' and s[i-1] not in '2357':
                res = (res + sol(i+minLength, k-1)) % 1000000007
            return res % 1000000007
        if s[0] not in '2357' or s[-1] in '2357':
            return 0
        res = sol(minLength, k-1) % 1000000007
        sol.cache_clear()
        return res
            