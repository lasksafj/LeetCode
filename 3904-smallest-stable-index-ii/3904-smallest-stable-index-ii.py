class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        R = nums[:]
        for i in range(len(nums)-2,-1,-1):
            R[i] = min(nums[i], R[i+1])
        ma = 0 
        for i in range(len(nums)):
            ma = max(ma, nums[i])
            if ma-R[i] <= k:
                return i
        return -1