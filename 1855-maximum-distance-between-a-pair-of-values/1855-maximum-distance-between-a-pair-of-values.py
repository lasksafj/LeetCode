class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        M,N = len(nums1),len(nums2)
        res = 0
        i,j = 0,0
        while i < M or j < N:
            if i < M and j < N and nums1[i] <= nums2[j]:
                res = max(res, j-i)
                j += 1
            else:
                if i < M:
                    i += 1
                else:
                    break
        return res