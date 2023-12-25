class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * 3
        dp[0] = dp[1] = 1
        for i in range(1, len(s)):
            dp[(i+1)%3] = 0
            if s[i] > '0':
                dp[(i+1)%3] += dp[i%3]
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] < '7'):
                dp[(i+1)%3] += dp[(i-1)%3]
            if dp[(i+1)%3] == 0:
                return 0
            
        return dp[len(s)%3]