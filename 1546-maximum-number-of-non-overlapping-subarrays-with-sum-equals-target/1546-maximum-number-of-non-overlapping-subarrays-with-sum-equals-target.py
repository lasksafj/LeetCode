class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cur = 0
        dp = [0]*len(nums)
        L = {}
        for i,x in enumerate(nums):
            cur += x         
            if cur == target:
                dp[i] = 1
            dp[i] = max(dp[i], dp[i-1])
            if cur-target in L:
                dp[i] = max(dp[i], dp[L[cur-target]] + 1)
            L[cur] = i
        return dp[-1]