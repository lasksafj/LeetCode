class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        pb = -1
        for a,b in sorted(intervals, key=lambda x: [x[0], -x[1]]):
            if b <= pb:
                res += 1
            else:
                pb = b
        return len(intervals)-res