class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        i = 0
        j = inf
        while n:
            if n&1:
                res = max(res, i-j)
                j = i
            i += 1
            n >>= 1
        return res