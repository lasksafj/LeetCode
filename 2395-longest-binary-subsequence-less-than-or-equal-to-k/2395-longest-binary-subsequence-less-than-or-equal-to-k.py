class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        d = 0
        res = 0
        for i in range(len(s)):
            d = (d<<1)|int(s[i])
            if d <= k:
                res += 1
            else:
                d ^= 1<<(int(log(d, 2)))
        return res