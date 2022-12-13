class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = matrix[0][:]
        prev = dp[:]
        for i in range(1, m):
            for j in range(n):
                a = prev[j]
                prev[j] = inf
                dp[j] = min(prev) + matrix[i][j]
                prev[j] = a
            prev = dp[:]
        return min(dp)