class Solution:
    def countCommas(self, n: int) -> int:
        p = 3
        res = 0
        while n >= 10**p:
            n -= 10**p
            p += 3
            res += n%(10**p) + 1
        return res