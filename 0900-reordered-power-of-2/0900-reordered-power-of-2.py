class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1: return True
        n = str(n)
        for d in permutations(n, len(n)):
            if d[0] == '0' or d[-1] in ['1','3','5','7','9']: continue
            d = int(''.join(d))
            if d&(d-1) == 0:
                return True
        return False