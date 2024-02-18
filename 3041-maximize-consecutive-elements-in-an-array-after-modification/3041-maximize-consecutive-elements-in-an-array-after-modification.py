class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        for n in nums:
            dp[n+1] = dp[n]+1
            dp[n] = dp[n-1]+1
                
        return max(dp.values())