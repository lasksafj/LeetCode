class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l,r = intervals[0]
        res = []
        for a,b in intervals[1:]:
            if a <= r:
                r = max(r, b)
            else:
                res.append([l,r])
                l = a
                r = b
        res.append([l,r])
        return res