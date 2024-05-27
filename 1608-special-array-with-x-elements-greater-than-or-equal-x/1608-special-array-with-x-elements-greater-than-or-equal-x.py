class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for n in nums:
            if n >= len(nums)-i and (i==0 or len(nums)-i > nums[i-1]):
                return len(nums)-i
            i += 1
        return -1