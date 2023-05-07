class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = [[0]*(k+1) for _ in range(len(nums))]
        pre = [0] * (len(nums))
        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] + nums[i]
        for i in range(len(nums)):
            dp[i][1] = pre[i]/(i+1)
            for j in range(i):
                for l in range(2,min(i+1,k)+1):
                    dp[i][l] = max(dp[i][l], (pre[i] - pre[j])/(i-j) + dp[j][l-1])
        return max(dp[i])