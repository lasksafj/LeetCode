class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        @cache
        def f(k):
            if k == 0:
                return 1
            return 2 * f(k - 1) + 1
        
        k = len(bin(n)[2:])-1
        nn = n^(1<<k)
        return f(k) - self.minimumOneBitOperations(nn)