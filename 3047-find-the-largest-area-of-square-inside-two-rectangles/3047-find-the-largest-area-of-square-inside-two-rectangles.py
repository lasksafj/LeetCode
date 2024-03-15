class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        N = len(bottomLeft)
        res = 0
        for i in range(N):
            for j in range(i):
                l,r = i,j
                if bottomLeft[l][0] > bottomLeft[r][0]:
                    l,r = r,l
                if topRight[l][0] <= bottomLeft[r][0]:
                    continue
                w = min(topRight[l][0], topRight[r][0]) - bottomLeft[r][0]
                if bottomLeft[l][1] > bottomLeft[r][1]:
                    l,r = r,l
                if topRight[l][1] <= bottomLeft[r][1]:
                    continue
                h = min(topRight[l][1], topRight[r][1]) - bottomLeft[r][1]
                res = max(res, min(h,w))
        return res*res