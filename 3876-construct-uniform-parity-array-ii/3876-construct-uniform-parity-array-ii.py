class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1)&1 == 1 or all(n&1==0 for n in nums1)