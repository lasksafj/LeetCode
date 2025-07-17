class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [[1]*k for _ in range(N)]
        for i in range(N):
            for j in range(i):
                m = (nums[i]+nums[j])%k
                dp[i][m] = max(dp[i][m], dp[j][m] + 1)
        return max(max(row) for row in dp)