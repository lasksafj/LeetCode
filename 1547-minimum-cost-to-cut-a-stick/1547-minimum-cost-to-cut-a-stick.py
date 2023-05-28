class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        print(cuts)
        @cache
        def sol(l,r):
            a = bisect_right(cuts, l)
            b = bisect_left(cuts, r)
            if a == b:
                return 0
            res = inf
            for i in range(a,b):
                m = cuts[i]
                if m == l or m == r:
                    continue
                res = min(res, sol(l,m) + sol(m,r))
            return res + r-l
        return sol(0,n)