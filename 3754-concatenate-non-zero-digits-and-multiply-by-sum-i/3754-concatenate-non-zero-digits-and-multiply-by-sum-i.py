class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = sum(int(c) for c in str(n))
        x = ''.join(c for c in str(n) if c != '0')
        if x: x = int(x)
        else: x = 0
        return x*s