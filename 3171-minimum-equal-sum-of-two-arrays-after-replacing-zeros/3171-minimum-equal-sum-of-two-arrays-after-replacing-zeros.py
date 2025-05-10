class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        if zero1 > zero2:
            zero1, zero2 = zero2, zero1
            s1, s2 = s2,s1
        if zero1 == zero2 == 0 and s1 != s2:
            return -1
        if zero1 == 0 and s2 + zero2 > s1:
            return -1
        return max(s1 + zero1, s2 + zero2)