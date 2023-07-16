class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = [-1] + nums1
        nums2 = [-1] + nums2
        @cache
        def dfs(i,d):
            if i == len(nums1):
                return 0
            if d == 0:
                prev1,prev2 = nums1[i-1],nums2[i-1]
            else:
                prev1,prev2 = nums2[i-1],nums1[i-1]
            if nums1[i] <= prev1 or nums2[i] <= prev2:
                return dfs(i+1, 1) + 1
            else:
                a = inf
                if nums1[i] > prev2 and nums2[i] > prev1:
                    a = dfs(i+1, 1) + 1
                return min(dfs(i+1, 0), a)
        return dfs(1,0)
                