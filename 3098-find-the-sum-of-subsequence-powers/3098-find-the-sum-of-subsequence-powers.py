class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(j,i,mi,k):
            if k == 0:
                return mi
            if i == len(nums):
                return 0
            res = dfs(j,i+1,mi,k) % MOD
            if j >= 0 and nums[i]-nums[j] < mi:
                return (res + dfs(i,i+1, nums[i]-nums[j], k-1)) % MOD
            return (res + dfs(i,i+1,mi, k-1)) % MOD
        nums.sort()
        return dfs(-1,0,inf,k)