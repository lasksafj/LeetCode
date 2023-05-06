class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 1000000007
        nums.sort()
        l,r = 0, len(nums)-1
        res = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + pow(2,(r-l),mod)) % mod
                l += 1
            else:
                r -= 1
        return res