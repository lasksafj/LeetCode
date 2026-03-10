MOD = 10**9 + 7
n = 10**5
fact = [1] * (n + 1)
inv_fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD
inv_fact[n] = pow(fact[n], MOD - 2, MOD)  # Fermat's inverse
for i in range(n - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def combination(n, k):
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # number of way to distribute n items to k buckets: nCk
        @cache
        def S(n,k):
            res = 0
            d = 1
            for j in range(k+1):
                res += d * combination(k,j) * combination(n-j*limit-1, k-1)
                d *= -1
            return res % (10**9+7)
        a,b = zero,one
        if a > b: a,b = b,a
        res = 0
        for k in range(a+1):
            res += S(a, k) * (S(b, k-1) + 2*S(b, k) + S(b, k+1))
        return res % (10**9+7)