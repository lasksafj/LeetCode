class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = 0
        k = -inf
        for a,b in intervals:
            if a >= k:
                k = b
            else:
                res += 1
        return res