class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = {}
        res = -1
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = i
            else:
                res = max(res, i - m[s[i]] - 1)
        return res