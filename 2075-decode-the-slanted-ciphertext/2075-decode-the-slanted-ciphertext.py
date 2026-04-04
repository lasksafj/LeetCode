class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        m = rows
        n = len(encodedText)//m
        i,j = 0,0
        res = ''
        while j < n:
            a,b = i,j
            while a < m and b < n:
                res += encodedText[a*n+b]
                a += 1
                b += 1
            j += 1
        return res.rstrip()