class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        pref_nums = list(accumulate(nums, initial=0))
        pref_cost = list(accumulate(cost, initial=0))
        N = len(nums)
        def A(j):
            return pref_nums[j+1]
        def C(i,j):
            return pref_cost[j+1] - pref_cost[i]

        @cache
        def dp(i):
            if i == N:
                return 0
            res = inf
            for j in range(i, N):
                res = min(res, A(j) * C(i,j) + k * C(i,N-1) + dp(j+1))
            return res

        return dp(0)