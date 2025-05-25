class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        # dpm[t][i] = max(dpm[t][i-1] + nums[i], dp[t-1][i-m] + S(i-m+1, i)) // last subarr include i
        # dp[t][i] = max(dp[t][i-1], dpm[t][i])
        N = len(nums)
        pre = list(accumulate(nums, initial=0))
        def S(i,j):
            return pre[j+1] - pre[i]

        dp = [[-inf]*(N+1) for _ in range(k+1)]
        dpm = [[-inf]*(N+1) for _ in range(k+1)]
        for i in range(N+1):
            dpm[0][i] = 0
            dp[0][i] = 0

        for t in range(1, k+1):
            for i in range(t*m, N+1):
                dpm[t][i] = max(dpm[t][i-1] + nums[i-1], (dp[t-1][i-m] if i-m>=0 else -inf) + S(i-1-m+1, i-1))
                dp[t][i] = max(dp[t][i-1], dpm[t][i])

        # for r in dp:
        #     print(r)
        # print()
        # for r in dpm:
        #     print(r)
        return dp[k][N]