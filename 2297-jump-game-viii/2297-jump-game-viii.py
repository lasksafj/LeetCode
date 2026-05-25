class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        N = len(nums)
        dp = [inf]*N
        dp[0] = 0
        st1 = []
        st2 = []
        for i in range(N):
            while st1 and nums[st1[-1]] <= nums[i]:
                j = st1.pop()
                dp[i] = min(dp[i], dp[j] + costs[i])
            st1.append(i)
            while st2 and nums[st2[-1]] > nums[i]:
                j = st2.pop()
                dp[i] = min(dp[i], dp[j] + costs[i])
            st2.append(i)
        return dp[-1]