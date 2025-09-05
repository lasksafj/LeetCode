class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1,61):
            a = num1 - i*num2
            if a < i:
                continue
            if bin(a).count('1') <= i:
                return i
        return -1