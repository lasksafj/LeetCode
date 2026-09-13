class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = []
        B = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    A.append([i,j])
                if img2[i][j] == 1:
                    B.append([i,j])
        m = defaultdict(int)
        for ax,ay in A:
            for bx,by in B:
                m[(ax-bx,ay-by)] += 1
        res = 0
        for i in m:
            res = max(res, m[i])
            
        return res