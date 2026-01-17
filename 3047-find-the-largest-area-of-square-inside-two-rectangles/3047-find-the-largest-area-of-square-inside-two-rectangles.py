class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        def intersect(a1,a2,b1,b2):
            if a1 > b1:
                a1,a2,b1,b2 = b1,b2,a1,a2
            return max(0, min(b2,a2) - b1)
        N = len(bottomLeft)
        res = 0
        for i in range(N):
            a1,a2 = bottomLeft[i][0], topRight[i][0]
            b1,b2 = bottomLeft[i][1], topRight[i][1]
            for j in range(i):
                c1,c2 = bottomLeft[j][0], topRight[j][0]
                d1,d2 = bottomLeft[j][1], topRight[j][1]
                res = max(res, min(intersect(a1,a2,c1,c2), intersect(b1,b2,d1,d2))**2)
        return res