class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort()
        if restrictions and restrictions[0][0] == 1:
            restrictions = restrictions[1:]
        A = [[1,0]]
        for i, r in restrictions:
            j, h = A[-1]
            h += i-j
            A.append([i, min(h, r)])
        res = n - A[-1][0] + A[-1][1]
        for k in range(len(A)-1,0,-1):
            res = max(res, A[k][1])
            i1,h1 = A[k-1]
            i2,h2 = A[k]
            if i2-i1 < h1-h2:
                A[k-1][1] = h2+i2-i1
            else:
                h = (i2-i1+h1+h2)//2
                res = max(res, h)
        return res