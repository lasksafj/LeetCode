class Solution:
    def numberOfWays(self, corridor: str) -> int:
        no_s = corridor.count('S')
        if no_s&1 or no_s == 0:
            return 0
        s = 0
        d = 0
        res = 1
        for c in corridor:
            s += c == 'S'
            if s == 2:
                d += 1
            elif s == 3:
                res *= d
                s = 1
                d = 0
        return res % (10**9+7)