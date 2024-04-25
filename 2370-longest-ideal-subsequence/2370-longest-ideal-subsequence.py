class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26
        res = 0
        for i in range(len(s)):
            n = ord(s[i])-ord('a')
            ndp = dp[:]
            for pre_n in range(max(n-k, 0), min(n+k, 25)+1):
                ndp[n] = max(ndp[n], dp[pre_n]+1)
                res = max(res, ndp[n])
            dp = ndp
        return res