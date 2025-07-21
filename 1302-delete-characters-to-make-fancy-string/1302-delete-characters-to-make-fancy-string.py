class Solution:
    def makeFancyString(self, s: str) -> str:
        N = len(s)
        res = ''
        i = 0
        while i < N:
            j = i+1
            while j < N and s[i] == s[j]:
                j += 1
            res += s[i] * min(2, j-i)
            i = j
        return res