class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n > 1:
            if n == 3:
                return res+2
            if n&1:
                if (n>>1)&1 == 0:
                    n -= 1
                else:
                    n += 1
            else:
                n //= 2
            res += 1
        return res