class Solution:
    def maxProduct(self, n: int) -> int:
        A = sorted(str(n))
        return int(A[-1]) * int(A[-2])