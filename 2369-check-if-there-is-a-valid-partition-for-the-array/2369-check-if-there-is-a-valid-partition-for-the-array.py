class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i):
            if i == len(nums):
                return True
            if i+2 <= len(nums) and nums[i] == nums[i+1]:
                if dfs(i+2):
                    return True
            if i+3 <= len(nums) and ((nums[i] == nums[i+1] == nums[i+2]) or (nums[i]+1 == nums[i+1] and nums[i+1]+1 == nums[i+2])):
                return dfs(i+3)
            return False
        return dfs(0)
            