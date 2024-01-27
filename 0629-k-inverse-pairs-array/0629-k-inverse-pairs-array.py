class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1

        for i in range(1,n+1):
            s = 0
            ndp = [0]*(k+1)
            for kk in range(k+1):
                s = (s + dp[kk]) % MOD
                if kk-i >= 0:
                    s = (s - dp[kk-i]) % MOD
                ndp[kk] = s
            dp = ndp
        
            
        return dp[-1] % MOD