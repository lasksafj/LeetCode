class Solution:
    def maxProduct(self, n: int) -> int:
        A = sorted(map(int, str(n)))
        return A[-1] * A[-2]