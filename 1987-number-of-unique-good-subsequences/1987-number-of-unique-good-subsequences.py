class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        binary = binary
        n = len(binary)
        mod = 10**9+7
        dp = [[0]*2 for _ in range(n+1)]
        last = [n]*2
        for i in range(n-1,-1,-1):
            c = int(binary[i])
            if last[c] == n:
                dp[i][c] = (dp[i+1][c] + sum(dp[i+1]) + 1)%mod
            else:
                dp[i][c] = (dp[i+1][c] + sum(dp[i+1]) - sum(dp[last[c]+1]))%mod
            dp[i][c^1] = dp[i+1][c^1]
            last[c] = i
        return dp[0][1] + (last[0] < n)