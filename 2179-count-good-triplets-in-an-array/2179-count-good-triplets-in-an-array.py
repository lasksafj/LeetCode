class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from sortedcontainers import SortedList
        m = {}
        for i,n in enumerate(nums2):
            m[n] = i
        A = SortedList()
        s = 0
        res = 0
        A.add(m[nums1[0]])
        for n in nums1[1:]:
            s += 1
            A.add(m[n])
            l = A.bisect_left(m[n])
            # print(l, len(nums1)-1-m[n]-(s-l))
            res += l * (len(nums1)-1-m[n]-(s-l))
            
        return res