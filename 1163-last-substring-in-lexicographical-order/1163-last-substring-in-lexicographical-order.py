class Solution:
    def lastSubstring(self, s: str) -> str:
        ma = 'A'
        midx = len(s)-1
        for i in range(len(s)-1, -1, -1):
            if ma < s[i]:
                midx = i
                ma = s[i]
            elif ma == s[i]:
                j = i+1
                jm = midx + 1
                while j < midx and jm < len(s):
                    if s[j] < s[jm]:
                        break
                    elif s[j] > s[jm]:
                        j = midx-1
                    j += 1
                    jm += 1
                if j == midx or jm == len(s):
                    midx = i
        return s[midx:]
            