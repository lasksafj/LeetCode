class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            res = ''.join(sorted(s))
        else:
            i = 0
            res = s
            while i < len(s):
                s = s[1:] + s[0]
                res = min(res, s)
                i += 1
        return res