class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        n = len(ranges)
        l,r = -1,-1
        nor = 0
        for a,b in ranges:
            if a <= r:
                r = max(r, b)
            else:
                l = a
                r = b
                nor += 1
        return pow(2,nor,1000000007)