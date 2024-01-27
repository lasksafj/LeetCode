class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1,n+1):
            s = 0
            for kk in range(k+1):
                # for j in range(min(i,kk+1)):
                #     dp[i][kk] += dp[i-1][kk-j]
                    
                s = (s + dp[i-1][kk]) % MOD
                if kk-i >= 0:
                    s = (s - dp[i-1][kk-i]) % MOD
                dp[i][kk] = s
        
            
        return dp[-1][-1] % MOD