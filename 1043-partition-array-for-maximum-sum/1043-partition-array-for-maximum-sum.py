class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        dp = [0]*(N+1)
        for i in range(1,N+1):
            ma = 0
            for j in range(i-1,max(0,i-k)-1,-1):
                ma = max(ma, arr[j])
                dp[i] = max(dp[i], dp[j] + ma*(i-j))
        return dp[-1]