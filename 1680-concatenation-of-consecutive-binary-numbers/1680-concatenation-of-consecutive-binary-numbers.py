class Solution:
    def concatenatedBinary(self, n: int) -> int:
        l = 0
        res = 0
        MOD = 10**9+7
        for i in range(1, n+1):
            if i&(i-1) == 0:
                l += 1
            res = ((res << l) | i) % MOD
        return res