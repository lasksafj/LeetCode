class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s = sum(machines)
        N = len(machines)
        if s%N:
            return -1
        target = s//N
        # cur: no clothes needed for [:i]
        # if cur > 0: need cur time to get cur clothes from [i+1:]
        # if cur < 0: need cur time to give cur clothes for [i+1:]
        cur = 0
        res = 0
        for m in machines:
            cur = cur + m - target
            res = max(res, m-target, abs(cur))
        return res