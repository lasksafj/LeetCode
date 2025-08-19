class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        j = 0
        res = 0
        for i,n in enumerate(nums):
            if n == 0:
                res += i-j+1
            else:
                j = i+1
        return res