class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A = SortedList(nums1)
        res = []
        for n in nums2:
            p = A.bisect_right(n)
            if p == len(A):
                res.append(A.pop(0))
            else:
                res.append(A.pop(p))
        return res