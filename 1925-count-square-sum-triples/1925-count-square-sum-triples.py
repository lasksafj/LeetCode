# Euclid's Formula | Generate Pythagorean Triples
# u,v: positive integer
# u > v
# a = u^2 - v^2
# b = 2uv
# c = u^2 + v^2
# A triple is primitive if and only if:
# (u,v) are coprime, and
# (u,v) have opposite parity (odd−even,even−odd)
# The triples (ka,kb,kc) & (kb,ka,kc) for k=1,...,n/c are the valid Pythagorean triples!

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for u in range(2, int(sqrt(n)) + 1):
            for v in range(1, u):
                if (u - v) & 1 == 0 or gcd(u, v) != 1:
                    continue                    
                c = u * u + v * v
                if c > n:
                    continue
                res += 2 * (n // c)
        return res
