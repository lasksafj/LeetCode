class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1 = set(nums1)
        s2 = set(nums2)
        
        return min(len(s1|s2), min(len(s1), n//2) + min(len(s2), n//2))