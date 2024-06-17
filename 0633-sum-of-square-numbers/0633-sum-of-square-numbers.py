class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5)+1):
            b = sqrt(c-a**2)
            if b == int(b):
                return True
        return False