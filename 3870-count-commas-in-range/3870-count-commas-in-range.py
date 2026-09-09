class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        d = 10**3
        c = 1
        while n >= d:
            res += c * (min(n, d * 10**3) - d) + 1
            c += 1
            d *= 10**3
        return res