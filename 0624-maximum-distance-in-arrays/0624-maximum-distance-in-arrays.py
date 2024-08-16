class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        A = []
        res = 0
        mi,ma = arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            a,b = arr[0],arr[-1]
            res = max(res, abs(ma-a), abs(b-mi))
            mi,ma = min(mi, a), max(ma, b)
        return res