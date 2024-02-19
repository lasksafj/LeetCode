class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        N = len(nums)
        @cache
        def dfs(i,j,score):
            res = 0
            if i+1 < j and nums[i]+nums[i+1] == score:
                res = max(res, dfs(i+2,j,score) + 1)
            if i < j and nums[i]+nums[j] == score:
                res = max(res, dfs(i+1,j-1,score) + 1)
            if i+1 < j and nums[j]+nums[j-1] == score:
                res = max(res, dfs(i,j-2,score) + 1)
            return res

        return max(dfs(2,N-1,nums[0]+nums[1]), 
                   dfs(0,N-3,nums[-1]+nums[-2]),
                   dfs(1,N-2,nums[0]+nums[-1])) + 1