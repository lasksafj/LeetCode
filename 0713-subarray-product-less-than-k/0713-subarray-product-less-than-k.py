class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        j,res = 0,0
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            while j < i and prod >= k:
                prod //= nums[j]
                j += 1
            if prod < k:
                res += i-j+1
        return res