class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        A = [b-a for a,b in zip(nums1,nums2)]
        B = [a-b for a,b in zip(nums1,nums2)]
        def sol(A):
            s,res = 0,0
            for n in A:
                if s+n < 0:
                    s = 0
                else:
                    s += n
                    res = max(res, s)
            return res
        return max(sol(A)+sum(nums1), sol(B)+sum(nums2))