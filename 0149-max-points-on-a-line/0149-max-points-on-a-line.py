class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = defaultdict(int)
        res = 0
        for i in range(n):
            c = 0
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                a,b = x1-x2, y1-y2
                s = b/a if a != 0 else None
                # s = atan2(b,a)
                m[s] += 1
                c = max(c, m[s])
                # print(points[i],points[j],a,b, m[s])
            res = max(res, c+1)
            m.clear()

        return res