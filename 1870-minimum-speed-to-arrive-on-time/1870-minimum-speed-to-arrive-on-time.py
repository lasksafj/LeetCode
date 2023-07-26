class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1
        def check(x):
            h = 0
            for d in dist[:-1]:
                h += ceil(d/x)
            return h + dist[-1]/x <= hour
        l,r = 1,10**9
        while l < r:
            m = (l+r)//2
            if check(m):
                r = m
            else:
                l = m+1
        return l