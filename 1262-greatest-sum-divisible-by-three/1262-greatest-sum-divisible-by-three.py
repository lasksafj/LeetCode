class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @cache
        def dfs(i,m):
            if i == len(nums):
                return 0 if m == 0 else -inf
            return max(dfs(i+1, m), dfs(i+1, (m*10+nums[i])%3) + nums[i])
        return dfs(0,0)