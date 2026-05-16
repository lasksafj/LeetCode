class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l,r = 0,len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            mi = (l+r)//2
            if nums[mi] < nums[r]:
                r = mi
            elif nums[mi] > nums[r]:
                l = mi+1
            else:
                r -= 1
        return nums[l]