class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        def getmask(r):
            res = 0
            for i,a in enumerate(r):
                res |= a << i
            return res
        m = {}
        for i,r in enumerate(grid):
            m[getmask(r)] = i
        # print(m)
        for i,r in enumerate(grid):
            a = getmask(r)
            if a == 0:
                return [i]
            for b in range(1,pow(2,len(grid[0]))+1):
                if a&b == 0 and b in m:
                    return [i,m[b]]
        return []
            