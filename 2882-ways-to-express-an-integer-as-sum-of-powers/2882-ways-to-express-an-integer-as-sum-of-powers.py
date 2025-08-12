class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9+7
        dp = [0]*(n+1)
        dp[0] = 1
        for a in range(1, n+1):
            ax = a**x
            if ax > n: break
            # no need create ndp, b/c we make k n->0, it make sure that dp[k] is updated from old dp
            for k in range(n, ax-1, -1):
                dp[k] = (dp[k] + dp[k-ax]) % MOD
        return dp[-1]