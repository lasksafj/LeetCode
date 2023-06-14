class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def sol(A):
            n = len(A)
            dp = [0] * n
            for i,v in enumerate(A):
                dp[i] = max((dp[i-2] if i>=2 else 0) + v, dp[i-1] if i>=1 else 0)
            return dp[n-1]
        
        return max(sol(nums[:n-1]), sol(nums[1:]))