class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        N = len(nums)
        acc = [0]*(N+1)
        for i in range(1,N+1):
            acc[i] = acc[i-1] + nums[i-1]
        dp = [0]*(N+1)
        pre = [0]*(N+2)
        j = 0
        for i in range(1,N+1):
            j = max(j, pre[i])
            dp[i] = dp[j]+1
            p = bisect_left(acc, 2*acc[i] - acc[j])
            pre[p] = i
        return dp[-1]