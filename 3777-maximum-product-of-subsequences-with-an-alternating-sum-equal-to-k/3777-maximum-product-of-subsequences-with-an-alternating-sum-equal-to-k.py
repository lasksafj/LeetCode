class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        @cache
        def dfs(i, s, p, sign, empty):
            if i == len(nums):
                if s == k and p <= limit and not empty:
                    return p
                return -1
            return max(
                dfs(i+1, s, p, sign, empty),
                dfs(i+1, s + sign*nums[i], min(limit+1, p*nums[i]), sign*-1, False)
            )
        res = dfs(0, 0, 1, 1, 1)
        dfs.cache_clear()
        return res