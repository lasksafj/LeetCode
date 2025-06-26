class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        no0 = 0
        A = [0]*(len(s)+1)
        for i in range(len(s)):
            no0 += s[i] == '0'
            A[i+1] = no0
        j = len(s)-1
        d = 0
        res = 0
        for i in range(len(s)-1,-1,-1):
            d = d | (int(s[i]) << (j-i))
            while d > k:
                d >>= 1
                j -= 1
            res = max(res, j-i+1 + A[i])
        return res