class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
#         dp = [[0]*k for _ in range(n)]
        
#         for i in range(n):
#             dp[i][0] = 1
#             for j in range(1, k):
#                 dp[i][j] = dp[i-1][j] + (dp[i-1][j-nums[i]] if j >= nums[i] else 0)
#         print(dp)
        if sum(nums) < k*2:
            return 0
            
        dp = [0] * k
        dp[0] = 1
        for i in range(n):
            for j in range(k-1, nums[i]-1, -1):
                dp[j] = dp[j] + dp[j-nums[i]]
        # print(dp)
        return (2**n - 2*sum(dp)) % 1000000007