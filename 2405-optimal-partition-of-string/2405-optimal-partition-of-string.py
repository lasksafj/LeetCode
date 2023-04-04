class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        m = {}
        for c in s:
            if c in m:
                m = {}
                res += 1
            m[c] = True
        return res