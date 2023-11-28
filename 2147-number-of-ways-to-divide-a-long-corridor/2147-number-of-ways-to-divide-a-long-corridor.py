class Solution:
    def numberOfWays(self, corridor: str) -> int:
        N = len(corridor)
        mod = 10**9+7
        zero,one,two = 0,0,1
        for c in corridor:
            if c == 'S':
                zero = one
                one,two = two,one
            else:
                two = (zero + two) % mod
        return zero