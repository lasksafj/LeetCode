class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        N = len(nums)
        res = 0
        dp = [[0]*(k+1) for _ in range(N+1)]
        dp[0][0] = 1
        for i,n in enumerate(nums):
            prev_dp = [row[:] for row in dp]
            for l in range(1, i+2):
                for s in range(n, k+1):
                    dp[l][s] += prev_dp[l-1][s-n]
            prev_dp = dp
            
        for l in range(1, N+1):
            res = (res + dp[l][k] * pow(2, N-l, MOD)) % MOD

        return res