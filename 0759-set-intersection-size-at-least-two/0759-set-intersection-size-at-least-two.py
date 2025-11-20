class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda e:[e[1], -e[0]])
        a,b = -1,-1
        res = 0
        for l,r in intervals:
            if b < l:
                res += 2
                a,b = r-1,r
            elif b >= l:
                if a < l:
                    a,b = b,r
                    res += 1
        return res