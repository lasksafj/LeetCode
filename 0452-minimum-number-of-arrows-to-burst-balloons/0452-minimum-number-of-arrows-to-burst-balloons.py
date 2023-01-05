class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        r = -inf
        res = 0
        for a,b in points:
            if a > r:
                r = b
                res += 1
        return res