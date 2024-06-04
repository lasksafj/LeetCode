class Solution:
    def minEnd(self, n: int, x: int) -> int:
        a = 1
        n -= 1
        res = x
        while n:
            if a&x == 0:
                if n&1:
                    res |= a 
                n >>= 1
            a <<= 1
        return res