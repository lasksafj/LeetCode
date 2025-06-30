class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        MOD = 10**9+7
        nums.sort()
        i,j = 0,len(nums)-1
        while i <= j:
            if nums[i] + nums[j] <= target:
                res = (res + pow(2, j-i, MOD)) % MOD
                i += 1
            else:
                j -= 1
        return res