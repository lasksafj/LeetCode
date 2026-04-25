class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        A = []
        for x,y in points:
            if y == 0:
                A.append(x)
            elif x == side:
                A.append(x+y)
            elif y == side:
                A.append(2*side + side-x)
            else:
                A.append(3*side + side-y)
        A.sort()
        N = 4*side
        def check(d):
            for i,first in enumerate(A):
                cnt = 1
                while cnt < k:
                    j = bisect_left(A, A[i]+d)
                    if j == len(A): break
                    if N-A[j]+first < d: break
                    i = j
                    cnt += 1
                if cnt >= k: return True
            return False
        l,r = 0,4*side
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                l = mi+1
            else:
                r = mi-1
        return r