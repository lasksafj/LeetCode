class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        prev = 0
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[i] == s[j]:
                j += 1
            res += min(prev, j-i)
            prev = j-i
            i = j
        return res