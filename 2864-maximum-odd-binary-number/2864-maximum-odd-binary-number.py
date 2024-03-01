class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a = s.count('1')
        res = []
        for _ in range(len(s)-1):
            if a-1:
                res.append('1')
                a -= 1
            else:
                res.append('0')
        res.append('1')
        return ''.join(res)