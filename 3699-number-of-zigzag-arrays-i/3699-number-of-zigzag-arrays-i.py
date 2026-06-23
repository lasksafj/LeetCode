class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9+7
        M = r-l+1
        dp0 = [1]*M
        dp1 = [1]*M
        for i in range(1, n):
            pref_inc = list(accumulate(dp0, initial=0))
            pref_dec = list(accumulate(dp1, initial=0))
            s_inc = pref_inc[-1]
            dp1 = [(s_inc - x) % MOD for x in pref_inc[1:]]
            dp0 = [x%MOD for x in pref_dec[:-1]]
        return (sum(dp0) + sum(dp1)) % MOD