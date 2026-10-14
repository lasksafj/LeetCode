class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        A = [abs(a-b) for a,b in zip(nums1,nums2)]
        def check(mi):
            k = 0
            for a in A:
                k += max(0, a-mi)
            return k <= k1+k2
        l,r = 0,max(A)
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        if l == 0: return 0
        k = k1+k2
        for i,a in enumerate(A):
            if a > l:
                k -= a-l
                A[i] = l
        res = 0
        for a in A:
            if k and a == l:
                a -= 1
                k -= 1
            res += a**2
        return res