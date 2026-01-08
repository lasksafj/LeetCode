class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        M,N = len(nums1),len(nums2)
        dp = [[-inf]*(N+1) for _ in range(M+1)]
        for i in range(1,M+1):
            for j in range(1,N+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + max(0, nums1[i-1]* nums2[j-1]), nums1[i-1]* nums2[j-1])
        return dp[-1][-1]