class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        a = 0
        b = 0
        while k > 1:
            if k%2:
                k += 1
                b += 1
            k //= 2
            a += 1
        return 1-a%2 if b%2 else a%2