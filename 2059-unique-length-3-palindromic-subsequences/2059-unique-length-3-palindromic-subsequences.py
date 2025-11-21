class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in range(26):
            l = s.find(chr(c+97))
            r = s.rfind(chr(c+97))
            if l >= r: continue
            res += len(set(s[l+1:r]))
        return res