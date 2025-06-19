class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        l = nums[0]
        for i,n in enumerate(nums):
            if i and n > nums[i-1] and n - l > k:
                res += 1
                l = n
        return res