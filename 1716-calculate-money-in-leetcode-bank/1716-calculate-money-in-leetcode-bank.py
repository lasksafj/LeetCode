class Solution:
    def totalMoney(self, n: int) -> int:
        k =n//7
        f = (1+2+3+4+5+6+7)
        l = (1+2+3+4+5+6+7) + (k-1)*7
        s = (f+l)*k//2
        d = k
        for _ in range(n%7):
            d += 1
            s += d
        return s