class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2*k:
            return 0
        n = len(nums)
        dp = [[0]*k for _ in range(n)]
        dp[0][0] = 1
        for j in range(1, k):
            dp[0][j] = (1 if nums[0] == j else 0)
        for i in range(1, n):
            dp[i][0] = 1
            for j in range(1, k):
                dp[i][j] = dp[i-1][j] + (dp[i-1][j-nums[i]] if j >= nums[i] else 0)

        return (2**n - 2*sum(dp[-1])) % 1000000007