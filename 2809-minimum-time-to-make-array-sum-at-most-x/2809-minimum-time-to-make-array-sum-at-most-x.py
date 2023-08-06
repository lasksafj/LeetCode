class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        N = len(nums1)
        p = sorted(list(range(N)), key=lambda x:nums2[x])
        nums1 = [nums1[i] for i in p]
        nums2 = [nums2[i] for i in p]
        s1 = sum(nums1)
        if s1 <= x:
            return 0
        s2 = sum(nums2)

        dp = [[0]*(N+1) for _ in range(N)]
        dp[0][1] = nums1[0] + nums2[0]
        for i in range(1,N):
            for j in range(1,i+2):
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j-1] + nums2[i]*j + nums1[i])
        for t in range(1, N+1):
            if s1 + s2*t - dp[N-1][t] <= x:
                return t
        return -1