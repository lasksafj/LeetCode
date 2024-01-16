class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for x in range(60):
            n = num1-x*num2
            if n < 1:
                return -1
            a = bin(n)[2:]
            no1 = a.count('1')
            if no1 > x:
                continue
            if n >= x:
                return x
        return -1