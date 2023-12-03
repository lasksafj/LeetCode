class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        pa,pb = points[0]
        for a,b in points[1:]:
            res += max(abs(a-pa),abs(b-pb))
            pa,pb = a,b
        return res