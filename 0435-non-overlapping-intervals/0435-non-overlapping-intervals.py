class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        def overlapping(a,b):
            return b[0] < a[1]
        res = 0
        i = 0
        n = len(intervals)
        while i < n:
            j = i+1
            while j < n and overlapping(intervals[i], intervals[j]):
                if intervals[j][1] < intervals[i][1]:
                    i = j
                j += 1
                res += 1
            i = j
        return res