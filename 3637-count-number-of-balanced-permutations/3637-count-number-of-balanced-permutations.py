MOD = 10**9+7
n = 80
fac = [0]*(n+1)
inv_fac = [0]*(n+1)
fac[0] = inv_fac[0] = 1
for i in range(1, n+1):
    fac[i] = fac[i-1] * i % MOD
inv_fac[n] = pow(fac[n], MOD - 2, MOD)
for i in range(n - 1, 0, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        N = len(num)
        A = [0]*10
        s = 0
        for a,b in Counter(num).items():
            a = int(a)
            A[a] = b
            s += a*b
        if s&1:
            return 0
        @cache
        def dfs(i, odd_s, odd_l):
            if odd_s > s//2 or odd_l > (N+1)//2:
                return 0
            if i == -1:
                if odd_s < s//2 or odd_l < (N+1)//2:
                    return 0
                return (fac[odd_l] * fac[N-odd_l]) % MOD
            res = 0
            for d in range(A[i]+1):
                res = (res + dfs(i-1, odd_s + i*d, odd_l + d) * inv_fac[d] * inv_fac[A[i]-d]) % MOD
            return res
        return dfs(9, 0, 0)