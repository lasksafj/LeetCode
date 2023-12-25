class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0]*(N+1) for _ in range(N+1)]
        for l in range(1, N+1):
            for i in range(N):
                j = i+l-1
                if j >= len(nums):
                    continue
                for k in range(i,j+1):
                    a = nums[i-1] if i-1 >= 0 else 1
                    b = nums[j+1] if j+1 < N else 1
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + a*nums[k]*b)
        return dp[0][N-1]