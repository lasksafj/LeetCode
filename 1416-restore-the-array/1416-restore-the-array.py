class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
            num = int(s[i])
            j = i+1
            while j <= n and num <= k:
                dp[i] += dp[j]
                num = num*10 + (int(s[j]) if j < n else 0)
                j += 1
            dp[i] %= 1000000007
        return dp[0]
                