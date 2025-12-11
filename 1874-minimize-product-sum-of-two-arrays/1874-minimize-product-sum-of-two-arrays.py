class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(reverse=True)
        nums2.sort()
        return sum(a*b for a,b in zip(nums1, nums2))