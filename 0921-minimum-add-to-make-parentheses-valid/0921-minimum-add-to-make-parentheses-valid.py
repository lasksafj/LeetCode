class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        d = 0
        for ch in s:
            if ch == '(':
                d += 1
            else:
                d -= 1
            if d < 0:
                res += (-d)
                d = 0
        return res + d