class Solution:
    def distinctSubseqII(self, s: str) -> int:
        s = '#' + s
        n = len(s)
        dp = [0]*n
        dp2 = [0]*n
        last = {}
        for i in range(1,n):
            dp[i] = dp[i-1]*2 + 1 - (dp2[last[s[i]]] if s[i] in last else 0)
            dp2[i] = dp[i-1] + 1 - (dp2[last[s[i]]-1] if s[i] in last else 0)
            last[s[i]] = i
        return dp[-1]