class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = matrix[0][:]
        prev = dp[:]
        for i in range(1, m):
            for j in range(n):
                dp[j] = min(prev[j-1] if j>0 else inf, prev[j], prev[j+1] if j<n-1 else inf) + matrix[i][j]
            prev = dp[:]
        return min(dp)