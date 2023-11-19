class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        def sol(m1,m2):
            res = 0
            for i in range(N-2,-1,-1):
                a,b = nums1[i],nums2[i]
                swap = 0
                if a > m1 and b > m1:
                    return inf
                elif a > m1:
                    a,b = b,a
                    swap = 1
                    res += 1
                if a > m2 and b > m2:
                    return inf
                elif b > m2:
                    if swap or b > m1:
                        return inf
                    res += 1
            return res
        res = min(sol(nums1[-1],nums2[-1]), sol(nums2[-1],nums1[-1]) + 1)
        return res if res < inf else -1