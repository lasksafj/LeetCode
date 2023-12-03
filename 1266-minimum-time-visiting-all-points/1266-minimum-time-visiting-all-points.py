class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        pa,pb = points[0]
        for a,b in points[1:]:
            mi = min(abs(a-pa),abs(b-pb))
            res += mi + abs(a-pa)-mi + abs(b-pb)-mi
            pa,pb = a,b
        return res