class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(x):
            res = 0
            for n in piles:
                res += ceil(n/x)
            return res <= h
        l,r = 1,h*max(piles)+1
        while l < r:
            m = (l+r)//2
            if check(m):
                r = m
            else:
                l = m+1
        return l