class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        N = len(stoneValue)
        pre = list(accumulate(stoneValue, initial=0))

        dp = [[0]*N for _ in range(N)]
        dp_max_L = [[0]*N for _ in range(N)]
        dp_max_R = [[0]*N for _ in range(N)]

        for j in range(N):
            p = j
            cur_R = 0
            for i in range(j, -1, -1):
                cur = pre[j+1] - pre[i]
                while cur >= (cur_R + stoneValue[p])*2:
                    cur_R += stoneValue[p]
                    p -= 1
                cur_L = cur - cur_R
                if i < j:
                    if cur_L == cur_R:
                        dp[i][j] = max(dp_max_L[i][p], dp_max_R[p+1][j])
                    else:
                        dp[i][j] = max(
                            dp_max_L[i][p-1] if p-1 >= i else 0, 
                            dp_max_R[p+1][j] if p+1 <= j else 0
                        )
                    
                if i == j:
                    dp_max_L[i][j] = stoneValue[i]
                    dp_max_R[i][j] = stoneValue[i]
                else:
                    dp_max_L[i][j] = max(dp_max_L[i][j-1], dp[i][j] + pre[j+1] - pre[i])
                    dp_max_R[i][j] = max(dp_max_R[i+1][j], dp[i][j] + pre[j+1] - pre[i])
        return dp[0][N-1]