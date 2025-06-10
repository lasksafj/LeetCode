class Solution:
    def maxDifference(self, s: str) -> int:
        mi,ma = inf,0
        for _,v in Counter(s).items():
            if v&1:
                ma = max(ma, v)
            else:
                mi = min(mi, v)
        return ma-mi