class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        N = len(stoneValue)
        pre = list(accumulate(stoneValue, initial=0))

        dp = [[0]*N for _ in range(N)]
        dp_max_L = [[0]*N for _ in range(N)]
        dp_max_R = [[0]*N for _ in range(N)]

        for j in range(N):
            for i in range(j, -1, -1):
                if i < j:
                    mi = (pre[j+1]+pre[i])//2
                    p = bisect_right(pre, mi)-1
                    l = pre[p]-pre[i]
                    r = pre[j+1]-pre[p]
                    if l < r:
                        dp[i][j] = dp_max_L[i][p-1]
                    elif l > r:
                        dp[i][j] = dp_max_R[p][j]
                    else:
                        dp[i][j] = max(dp_max_L[i][p-1], dp_max_R[p][j])
                    if p+1 <= j:
                        dp[i][j] = max(dp[i][j], dp_max_R[p+1][j])

                if i == j:
                    dp_max_L[i][j] = stoneValue[i]
                    dp_max_R[i][j] = stoneValue[i]
                else:
                    dp_max_L[i][j] = max(dp_max_L[i][j-1], dp[i][j] + pre[j+1] - pre[i])
                    dp_max_R[i][j] = max(dp_max_R[i+1][j], dp[i][j] + pre[j+1] - pre[i])
        return dp[0][N-1]