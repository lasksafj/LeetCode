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
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def dfs(i,p):
            res = 0
            for ne in adj[i]:
                if ne==p: continue
                res = max(res, dfs(ne,i))
            return res+1
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        d = dfs(1, 0)-1
        res = 0
        MOD = 10**9+7
        for i in range(1, d+1, 2):
            res = (res + combination(d,i)) % MOD
        return res