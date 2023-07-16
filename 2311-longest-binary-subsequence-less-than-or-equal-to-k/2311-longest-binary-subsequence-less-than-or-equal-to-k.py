class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        n = 0
        j = 0
        for i in range(len(s)):
            n = (n<<1)|(s[i]=='1')
            if n <= k:
                res += 1
            else:
                n ^= 1 << (int(log(n,2)))
        return res