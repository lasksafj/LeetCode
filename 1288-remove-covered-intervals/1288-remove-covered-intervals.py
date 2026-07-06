class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        pa,pb = -1,-1
        for a,b in sorted(intervals, key=lambda x: [x[0], -x[1]]):
            if pa <= a and b <= pb:
                res += 1
            else:
                pa,pb = a,b
        return len(intervals)-res