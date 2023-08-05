class Solution:
    def countDigitOne(self, n: int) -> int:
        i = 1
        res = 0
        while i <= n:
            d = i*10
            res += (n//d)*i + min(max(n%d - i + 1, 0), i)
            i *= 10
        return res