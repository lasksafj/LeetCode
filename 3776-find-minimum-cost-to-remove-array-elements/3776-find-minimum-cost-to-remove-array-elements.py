class Solution:
    def minCost(self, nums: List[int]) -> int:
        N = len(nums)
        @cache
        def dfs(prev, i):
            if i == N:
                return prev
            if i+1 == N:
                return max(prev ,nums[i])
            A = sorted([prev, nums[i], nums[i+1]])
            res = inf
            return min(dfs(A[0], i+2) + A[2], dfs(A[2], i+2) + A[1])
        return dfs(nums[0], 1)