class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7
        return (m * comb(n-1, k) * pow(m-1, n-1-k, MOD)) % MOD