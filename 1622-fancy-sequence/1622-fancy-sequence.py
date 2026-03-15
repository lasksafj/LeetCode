# A = [*a1, +a2, +a3, *a4]
# Every operation is treated as a linear function f(x) = ax + b
# Addition (+k): a = 1, b = k => f(x) = 1x + k
# Let P[i] = (ai, bi) be the cumulative function from the start to index i-1.
# P[i](x) = ai*x + bi
# P[n](x) = an*x + bn
# an*x + bn = A(ai*x + bi) + B
# an*x + bn = (A*ai)x + (A*bi + B)
# A = an/ai
# B = bn - (A*bi)
MOD = 10**9+7
class Fancy:

    def __init__(self):
        self.A = []
        self.a = 1
        self.b = 0

    def append(self, val: int) -> None:
        self.A.append([val, self.a, self.b])

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % MOD

    def multAll(self, m: int) -> None:
        self.a = (self.a*m) % MOD
        self.b = (self.b*m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.A): return -1
        ai,bi = self.A[idx][1:]
        an,bn = self.a, self.b
        A = an * pow(ai, MOD-2, MOD)
        B = (bn - (A*bi)) % MOD
        return (A*self.A[idx][0] + B) % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)