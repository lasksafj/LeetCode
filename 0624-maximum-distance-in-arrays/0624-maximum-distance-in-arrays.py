class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        A = []
        cur = 0
        mi,ma = inf,-inf
        for arr in arrays:
            a,b = arr[0],arr[-1]
            nmi,nma = min(a,b), max(a,b)
            cur = max(cur, ma-nmi, nma-mi)
            A.append(cur)
            mi,ma = min(mi, nmi), max(ma, nma)
        res = 0
        cur = 0
        mi,ma = inf,-inf
        for i in range(len(arrays)-1,-1,-1):
            arr = arrays[i]
            a,b = arr[0],arr[-1]
            nmi,nma = min(a,b), max(a,b)
            cur = max(cur, ma-nmi, nma-mi)
            res = max(res, A[i], cur)
            mi,ma = min(mi, nmi), max(ma, nma)
        return res