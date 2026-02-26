class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        res = 0
        while len(s) > 1:
            i = len(s)-2
            while i >= 0 and s[i] == s[i+1]:
                i -= 1
            if s[i+1] == '1':
                res += 1
                if i >= 0:
                    s[i] = '1'
            res += len(s)-i-1
            s = s[:i+1]
        return res