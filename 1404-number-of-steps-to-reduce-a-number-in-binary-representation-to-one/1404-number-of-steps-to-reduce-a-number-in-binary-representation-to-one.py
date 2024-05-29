class Solution:
    def numSteps(self, s: str) -> int:
        i = len(s)-1
        change = 0
        res = 0
        while i > 0:
            cur = (s[i] == '1') ^ change
            if cur == 1:
                res += 1
                change = 1
            res += 1
            i -= 1
        return res+change