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
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        @cache
        def dfs(i, mask, m, k):
            if m == 0:
                if k - bin(mask).count('1') != 0:
                    return 0
                return 1
            if i == len(nums):
                return 0
            
            res = 0
            for c in range(m+1):
                nmask = c + mask
                res = (res + dfs(i+1, nmask>>1, m-c, k-(nmask&1)) * pow(nums[i], c, MOD) * combination(m,c)) % MOD
            return res
        
        return dfs(0, 0, m, k)