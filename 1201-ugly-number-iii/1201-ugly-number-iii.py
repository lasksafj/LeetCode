class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def check(mi):
            return mi//a + mi//b + mi//c - mi//lcm(a,b) - mi//lcm(b,c) - mi//lcm(c,a) + mi//lcm(a,lcm(b,c)) >= n
        l,r = min(a,b,c),10**10
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l