def f(nums, score):
    dp = [[0]*len(nums) for _ in range(len(nums))]

    def dfs(i,j):
        if i >= j:
            return 0
        if dp[i][j] > 0:
            return dp[i][j]
        res = 0
        if i+1 < len(nums) and nums[i]+nums[i+1] == score:
            res = max(res, dfs(i+2,j) + 1)
        if nums[i]+nums[j] == score:
            res = max(res, dfs(i+1,j-1) + 1)
        if j >= 0 and nums[j]+nums[j-1] == score:
            res = max(res, dfs(i,j-2) + 1)
        dp[i][j] = res
        return res
    return dfs(0,len(nums)-1)

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        res = 0
        for score in [nums[0]+nums[1],nums[0]+nums[-1],nums[-1]+nums[-2]]:
            res = max(res, f(nums, score))
        return res