class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for (a,b),(c,d) in pairwise(points):
            res += max(abs(c-a), abs(d-b))
        return res