class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = []
        while n > 0:
            a = n%26
            if a == 0:
                res.append('Z')
                n -= 1
            else:
                res.append(chr(n%26 + ord('A') - 1))
            n //= 26
        return ''.join(res[::-1])