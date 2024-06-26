class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        @lru_cache
        def dfs(i):
            if i == len(nums):
                return [[]]
            res = []
            for a in dfs(i+1):
                res.append([nums[i]] + a)
                res.append(a)
            return res
        return dfs(0)