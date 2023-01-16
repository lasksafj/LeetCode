class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        l,r = newInterval
        ins = False
        for a,b in intervals:
            if b < l or a > r:
                if a > r and not ins:
                    res.append([l,r])
                    ins = True
                res.append([a,b])
            else:
                l = min(l,a)
                r = max(b,r)
        if not ins:
            res.append([l,r])
        return res