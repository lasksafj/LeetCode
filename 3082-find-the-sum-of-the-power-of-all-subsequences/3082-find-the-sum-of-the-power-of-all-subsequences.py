class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        N = len(nums)
        res = 0
        dp = [[0]*(k+1) for _ in range(N+1)]
        dp[0][0] = 1
        for i,n in enumerate(nums):
            for l in range(i+1, 0, -1):
                for s in range(k, n-1, -1):
                    dp[l][s] += dp[l-1][s-n]
            
        for l in range(1, N+1):
            res = (res + dp[l][k] * pow(2, N-l, MOD)) % MOD

        return res