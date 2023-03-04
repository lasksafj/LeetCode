class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        a = 4
        while n > 1:
            res += a
            a += 4
            n -= 1
        return res