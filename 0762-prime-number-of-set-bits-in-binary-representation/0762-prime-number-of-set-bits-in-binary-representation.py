class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def sol(n):
            i = 0
            p = []
            while n > 0:
                if n&1:
                    p.append(i)
                i += 1
                n >>= 1
            p = p[::-1]
            i = 0
            res = 0
            for k in [2,3,5,7,11,13,17,19]:
                for i in range(min(k+1, len(p))):
                    res += comb(p[i], k-i)
            return res
        return sol(right+1) - sol(left)