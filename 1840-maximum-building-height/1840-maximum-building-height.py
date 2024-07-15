class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort()
        # reduce each height in A to its highest possible -> result in A
        A = [[1,0]]
        for i,h in restrictions:
            li,lh = A[-1]
            A.append([i, min(lh+i-li, h)])
        for k in range(len(A)-2,-1,-1):
            i,h = A[k]
            ri,rh = A[k+1]
            h = min(h, rh+ri-i)
            A[k][1] = h
        res = 0
        # find max height between A[k-1] and A[k]
        # x: max height
        # li,lh = A[k-1]
        # i,h = A[k]
        # x-lh+x-h=i-li => 2x=h+lh+i-li
        for k in range(1,len(A)):
            li,lh = A[k-1]
            i,h = A[k]
            res = max(res, (h+lh+i-li)//2)
        
        return max(res, A[-1][1] + n-A[-1][0])