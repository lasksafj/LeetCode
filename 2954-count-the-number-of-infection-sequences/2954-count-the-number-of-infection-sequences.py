MOD = 10**9+7

# compute i!
@cache
def fact(i):
    return 1 if i < 2 else i*fact(i-1) % MOD

# compute 1/(i!)
@cache
def inv_fact(i):
    return pow(fact(i), -1, MOD)

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        res = fact(n - len(sick)) * inv_fact(sick[0]) * inv_fact(n - sick[-1] - 1) % MOD
        for i in range(len(sick)-1):
            a = sick[i]
            b = sick[i+1]
            if b > a+1:
                res = (res * inv_fact(b-a-1) * pow(2,b-a-2,MOD)) % MOD
        return res