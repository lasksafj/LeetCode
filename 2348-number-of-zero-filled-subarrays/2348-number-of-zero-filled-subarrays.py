class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums.append(1)
        l = -1
        res = 0
        for i,n in enumerate(nums):
            if n != 0:
                a = i-l
                res += a*(a-1)//2
                l = i
        return res