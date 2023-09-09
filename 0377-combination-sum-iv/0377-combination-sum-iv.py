class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(s):
            if s > target:
                return 0
            elif s == target:
                return 1
            res = 0
            for n in nums:
                res += dfs(s+n)
            return res
        return dfs(0)