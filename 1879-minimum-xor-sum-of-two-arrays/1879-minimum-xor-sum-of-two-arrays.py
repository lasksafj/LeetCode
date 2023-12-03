class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        @cache
        def dfs(i,mask):
            if i == N:
                return 0
            res = inf
            for j in range(N):
                if mask&(1<<j) == 0:
                    res = min(res, dfs(i+1,mask|(1<<j)) + (nums1[i]^nums2[j]))
            return res
        return dfs(0,0)