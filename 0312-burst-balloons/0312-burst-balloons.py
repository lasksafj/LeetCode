class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j]: max for (i,j) (not inclusive)
        # dp[i][j] = dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]
        nums = [1] + nums + [1]
        N = len(nums)
        dp = [[0]*N for _ in range(N)]
        for j in range(N):
            for i in range(j-2, -1, -1):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
        return dp[0][N-1]