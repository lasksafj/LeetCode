class Solution:
    def checkPartitioning(self, s: str) -> bool:
        N = len(s)
        dp = [[0]*N for _ in range(N)]
        for j in range(N):
            dp[j][j] = 1
            for i in range(j):
                if s[i] == s[j]:
                    dp[i][j] = j==i+1 or dp[i+1][j-1]
        for i in range(N):
            for j in range(i+2,N):
                if dp[0][i] and dp[j][N-1] and dp[i+1][j-1]:
                    return True
        
        return False