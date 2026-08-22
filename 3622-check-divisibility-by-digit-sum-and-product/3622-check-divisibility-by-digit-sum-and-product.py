class Solution:
    def checkDivisibility(self, n: int) -> bool:
        A = [int(c) for c in str(n)]
        return n % (sum(A) + prod(A))==0