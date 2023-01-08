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
                g = 0
                if a != 0 and b != 0:
                    g = gcd(a,b)
                    a,b = a//g, b//g
                    if (a*b < 0 and a > 0) or (a*b > 0 and a < 0):
                        a,b = -a,-b
                elif a == 0:
                    b = y1
                elif b == 0:
                    a = x1
                s = str(a) + '*' + str(b)
                m[s] += 1
                c = max(c, m[s])
                # print(points[i],points[j],a,b, m[s])
            res = max(res, c+1)
            m.clear()

        return res