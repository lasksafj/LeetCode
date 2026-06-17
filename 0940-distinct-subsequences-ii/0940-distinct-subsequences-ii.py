class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        mod = 10**9+7
        dp = [0]*(n+1)
        last = [0]*26
        for i,c in enumerate(s):
            i += 1
            c = ord(c)-ord('a')
            if last[c] == 0:
                dp[i] = (dp[i-1]*2 + 1)%mod
            else:
                dp[i] = (dp[i-1]*2 - dp[last[c]-1])%mod
            last[c] = i
        return dp[-1]