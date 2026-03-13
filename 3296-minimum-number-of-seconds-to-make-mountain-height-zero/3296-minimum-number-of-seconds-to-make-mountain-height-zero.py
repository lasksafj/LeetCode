class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(t):
            res = 0
            for w in workerTimes:
                res += int(sqrt(2*t/w + 1/4) - 1/2)
            return res >= mountainHeight
        l,r = 0, max(workerTimes) * (mountainHeight+1)*mountainHeight
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l