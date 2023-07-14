class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def getSum(i, T):
            s = 0
            i += 1
            while i > 0:
                s += T[i]
                i -= (i&-i)
            return s
        def update(i, v, T):
            i += 1
            while i < len(T):
                T[i] += v
                i += (i&-i)
        A = [0]*len(nums1)
        m = {}
        for i,n in enumerate(nums2):
            m[n] = i
        T = [0]*(len(nums1)+1)
        for i,n in enumerate(nums1):
            A[i] = getSum(m[n], T)
            update(m[n], 1, T)
        res = 0
        T = [0]*(len(nums1)+1)
        s = 0
        for i in range(len(nums1)-1, -1, -1):
            n = nums1[i]
            res += (s-getSum(m[n], T)) * A[i]
            update(m[n], 1, T)
            s += 1
        return res