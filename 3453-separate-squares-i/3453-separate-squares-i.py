class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        t = sum(l**2 for _,_ ,l in squares)/2
        def check(y):
            res = 0
            for a,b,l in squares:
                if b+l <= y:
                    res += l**2
                elif b < y < b+l:
                    res += (y-b)*l
            return res >= t
        l,r = 0,10**9
        eps = 1e-5
        while l <= r - eps:
            mi = (l+r)/2
            if check(mi):
                r = mi
            else:
                l = mi
        return l