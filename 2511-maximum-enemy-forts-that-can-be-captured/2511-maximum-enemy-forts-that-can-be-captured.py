class Solution:
    def captureForts(self, forts: List[int]) -> int:
        res = 0
        l = 100000
        for i,n in enumerate(forts):
            if n == 1 or n == -1:
                r = (i+1)*n
                if l<0 and r>0 or r<0 and l>0:
                    res = max(res, abs(r)-abs(l)-1)
                l = r
        return res
            