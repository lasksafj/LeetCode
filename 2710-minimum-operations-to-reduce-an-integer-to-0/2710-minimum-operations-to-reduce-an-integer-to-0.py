class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n:
            if n&1 == 0:
                n >>= 1
            elif n&2:
                n += 1
                res += 1
            else:
                n >>= 1
                res += 1
        return res