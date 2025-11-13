class Solution:
    def maxOperations(self, s: str) -> int:
        N = len(s)
        i = s.find('1')
        if i == -1: return 0
        d = 1
        res = 0
        while i < N:
            j = i+1
            while j < N and s[j] == '0':
                j += 1
            res += d if j-i > 1 else 0
            d += 1
            i = j
        return res