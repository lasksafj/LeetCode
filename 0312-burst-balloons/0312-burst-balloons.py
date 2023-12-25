class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j]: max point for (i,j)
        dp = defaultdict(lambda:defaultdict(int))
        for l in range(3, len(nums)+3):
            for i in range(-1,len(nums)):
                j = i+l-1
                if j > len(nums):
                    continue
                for k in range(i+1,j):
                    a = nums[i] if i >= 0 else 1
                    b = nums[j] if j < len(nums) else 1
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + a*nums[k]*b)
        return dp[-1][len(nums)]