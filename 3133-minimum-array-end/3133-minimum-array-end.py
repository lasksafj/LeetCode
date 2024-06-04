class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n = bin(n-1)[2:][::-1]
        x = bin(x)[2:][::-1]
        res = []
        i,j = 0,0
        while i < len(x) or j < len(n):
            if j < len(n) and (i >= len(x) or x[i] == '0'):
                res.append(n[j] == '1')
                j += 1
            else:
                res.append(x[i] == '1')
            i += 1
        ans = 0
        for i in res[::-1]:
            ans <<= 1
            ans |= i
        return ans