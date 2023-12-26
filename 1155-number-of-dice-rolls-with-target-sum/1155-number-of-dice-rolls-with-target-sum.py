class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        dp = [0]*(target+1)
        dp[0] = 1
        for d in range(n):
            ndp = [0]*(target+1)
            s = dp[0]
            for i in range(1,target+1):
                ndp[i] = s
                s = (s + dp[i]) % MOD
                if i >= k:
                    s = (s - dp[i-k]) % MOD
                
                # for j in range(1,min(i,k)+1):
                #     ndp[i] = (ndp[i] + dp[i-j]) % MOD
            dp = ndp
        return dp[target]