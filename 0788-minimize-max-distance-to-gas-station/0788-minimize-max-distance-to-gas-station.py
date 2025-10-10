class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def check(d):
            return sum( int((b-a)/d) for a,b in pairwise(stations)) <= k
        l,r = 0,10**8
        while r-l > 1e-6:
            mi = (l+r)/2
            if check(mi):
                r = mi
            else:
                l = mi
        return l