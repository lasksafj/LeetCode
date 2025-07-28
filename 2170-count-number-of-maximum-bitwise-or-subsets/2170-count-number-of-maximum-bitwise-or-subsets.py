class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            a |= n
        
        @cache
        def dfs(i, n):
            if i == len(nums):
                return n == a
            return dfs(i+1, n|nums[i]) + dfs(i+1, n)
        return dfs(0,0)