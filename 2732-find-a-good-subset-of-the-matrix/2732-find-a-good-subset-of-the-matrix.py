class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        def getmask(r):
            res = 0
            for i,a in enumerate(r):
                res |= a << i
            return res
        m = {}
        n = len(grid[0])
        for i,r in enumerate(grid):
            a = getmask(r)
            if a == 0:
                return [i]
            b = (2**n-1) ^ a
            c = b
            while c > 0:
                if c in m:
                    return [m[c],i]
                c = b&(c-1)
            m[a] = i
        return []
            