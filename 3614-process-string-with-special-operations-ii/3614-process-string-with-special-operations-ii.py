class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = 0
        k += 1
        for c in s:
            if c.isalpha():
                n += 1
            elif c == '*' and n:
                n -= 1
            elif c == '#':
                n *= 2
        if k > n: return '.'
        for c in s[::-1]:
            if c.isalpha():
                if n == k: 
                    return c
                n -= 1
            elif c == '*':
                n += 1
            elif c == '#':
                n //= 2
                if k > n:
                    k -= n
            else:
                k = n-k+1
        return '.'