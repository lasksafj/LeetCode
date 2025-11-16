class Solution:
    def numSub(self, s: str) -> int:
        s += '0'
        l = -1
        res = 0
        for i in range(len(s)):
            if s[i] == '0':
                res += (i-l-1) * (i-l) // 2
                l = i
        return res % (10**9+7)