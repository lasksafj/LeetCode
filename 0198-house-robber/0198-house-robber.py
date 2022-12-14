class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * 4
        for i in range(n):
            dp[i%4] = max(dp[(i-2)%4] if i-2>=0 else 0, dp[(i-3)%4] if i-3>=0 else 0) + nums[i]
        return max(dp[(n-1)%4], dp[(n-2)%4])