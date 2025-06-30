class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 1
        MOD = 10**9+7
        nums.sort()
        j = 0
        for i,n in enumerate(nums):
            j = bisect_left(nums, target-n+1, 0, i+1)
            if j <= i:
                res = (res + pow(2, i-j, MOD)) % MOD
        
        return (pow(2, len(nums), MOD) - res) % MOD