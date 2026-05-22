class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            mi = (l+r)//2
            if nums[mi] == target: return mi
            if nums[l] <= nums[mi]:
                if nums[l] <= target < nums[mi]:
                    r = mi-1
                else:
                    l = mi+1
            else:
                if nums[mi] < target <= nums[r]:
                    l = mi+1
                else:
                    r = mi-1
        return -1