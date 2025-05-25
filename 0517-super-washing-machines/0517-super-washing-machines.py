class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s = sum(machines)
        N = len(machines)
        if s%N:
            return -1
        t = s//N
        res = cur = 0
        for m in machines:
            cur += m-t
            res = max(res, m-t, abs(cur))
        return res