class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        N = len(s)
        dp = [[0]*N for _ in range(N)]
        for j in range(N):
            for i in range(j):
                dp[i][j] = (dp[i+1][j-1] if i+1<j else 0) + (s[i] != s[j])
        dp2 = [[inf]*(k+1) for _ in range(N)]
        for j in range(N):
            dp2[j][1] = dp[0][j]
            for d in range(2,k+1):
                for i in range(j):
                    dp2[j][d] = min(dp2[j][d], dp2[i][d-1] + dp[i+1][j])
            
        # for e in dp:
        #     print(e)
        # print()
        # for e in dp2:
        #     print(e)
        return dp2[N-1][k]