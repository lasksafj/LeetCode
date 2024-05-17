class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        default_val = (1<<32)-1
        
        @cache
        def dfs(i,j,cur):
            if i==len(nums) and j==len(andValues):
                return 0
            if i==len(nums) or j==len(andValues):
                return inf
            if cur < andValues[j]:
                return inf
            res = dfs(i+1,j,cur&nums[i])
            if cur&nums[i] == andValues[j]:
                res = min(res, dfs(i+1,j+1,default_val) + nums[i])
                
            return res
        
        res = dfs(0,0,default_val)
        return res if res < inf else -1