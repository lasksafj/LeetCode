class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(2**len(nums)):
            j = 0
            d = 0
            while i > 0:
                if i&1:
                    d ^= nums[j]
                j += 1
                i >>= 1
            res += d
        return res