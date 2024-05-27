class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        s1 = sum(nums1)
        s2 = sum(nums2)
        def check(start, skip, x):
            j = start
            for i in range(len(nums2)):
                while nums1[j] + x != nums2[i]:
                    skip -= 1
                    if skip < 0:
                        return False
                    j += 1
                j += 1
            return True
        
        if check(2, 0, nums2[0] - nums1[2]):
            return nums2[0] - nums1[2]
        if check(1, 1, nums2[0] - nums1[1]):
            return nums2[0] - nums1[1]
        return nums2[0] - nums1[0]
