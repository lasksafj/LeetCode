class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def flatten(p):
            x,y = p
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return side*3 - x
            if x == 0:
                return side*4 - y
        A = sorted(map(flatten, points))
        def check(mi):
            for i,n in enumerate(A):
                cnt = 1
                while cnt < k:
                    j = bisect_left(A, A[i] + mi)
                    if j == len(A):
                        break
                    if A[j] + mi - 4*side > n:
                        break
                    i = j
                    cnt += 1
                if cnt >= k:
                    return True
            return False
        l,r = 1, side
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                l = mi+1
            else:
                r = mi-1
        return r