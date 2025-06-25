class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        A = nums2
        B = [-n for n in nums2][::-1]
        def check(mi):
            res = 0
            for n in nums1:
                if n == 0:
                    res += len(A) if mi >= 0 else 0
                    continue
                if n >= 0:
                    res += bisect_right(A, mi//n)
                else:
                    res += bisect_right(B, mi//(-n))

            return res >= k

        l,r = -10**10,10**10
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l