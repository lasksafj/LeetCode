class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = -1
        for a,b,c in combinations(points, 3):
            res = max(res,
                abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]))
            )
        return res/2