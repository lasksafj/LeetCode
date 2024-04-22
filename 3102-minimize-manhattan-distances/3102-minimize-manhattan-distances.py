class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
#         xi - xj + yi - yj, xi - xj - yi + yj, - xi + xj + yi - yj, - xi + xj - yi + yj
#         xi+yi - (xj+yj), xi-yi - (xj-yj), -(xi-yi) + (xj-yj), -(xi+yi) + (xj+yj)
#         a1 = xi+yi, b1 = xj+yj, a2 = xi-yi, b2= xj-yj
#         a1 - b1, a2 - b2, -a2 + b2, -a1 + b1
        
#         [x,y] -> [x-y,x+y], a=x-y, b=x+y, max_dist = max(max(a) - min(a), max(b) - min(b)) for all i
        A = []
        B = []
        for x,y in points:
            a = x-y
            b = x+y
            A.append(a)
            B.append(b)
        A.sort()
        B.sort()
        # print(A)
        # print(B)
        res = inf
        for x,y in points:
            a = x-y
            b = x+y
            ma1 = A[-1] - A[0]
            ma2 = B[-1] - B[0]
            if a == A[0]:
                ma1 = A[-1] - A[1]
            elif a == A[-1]:
                ma1 = A[-2] - A[0]
            if b == B[0]:
                ma2 = B[-1] - B[1]
            elif b == B[-1]:
                ma2 = B[-2] - B[0]
            res = min(res, max(ma1, ma2))
        return res