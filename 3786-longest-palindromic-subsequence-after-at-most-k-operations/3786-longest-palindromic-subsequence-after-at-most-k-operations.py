class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        A = [ord(c)-97 for c in s]
        N = len(A)
        dp = [[[0]*(k+1) for _ in range(N)] for _ in range(N)]
        
        def dfs(i,j,k):
            if i > j:
                return 0
            if i == j:
                return 1
            if dp[i][j][k]:
                return dp[i][j][k]
            res = max(dfs(i+1, j, k), dfs(i, j-1, k))
            a,b = A[i],A[j]
            if b > a:
                a,b = b,a
            op = min(a-b, b+26-a)
            if op <= k:
                res = max(res, dfs(i+1, j-1, k-op) + 2)
            dp[i][j][k] = max(res, 1)
            return dp[i][j][k]
        return dfs(0,len(A)-1,k)