class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i,j,t):
            if i > j:
                return 0
            if t:
                return max(dfs(i+1,j,t^1) + nums[i], dfs(i,j-1,t^1) + nums[j])
            else:
                return min(dfs(i+1,j,t^1), dfs(i,j-1,t^1))
        # print(dfs(0,len(nums)-1,1))
        return dfs(0,len(nums)-1,1) >= sum(nums)/2