class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        m1 = Counter(nums1)
        m2 = Counter(nums2)
        res = [set() for _ in range(2)]
        for a in nums1:
            if a not in m2:
                res[0].add(a)
        for b in nums2:
            if b not in m1:
                res[1].add(b)
        return res