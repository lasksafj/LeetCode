class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        m = {}
        res = 0
        s = 0
        for n in rolls:
            if n not in m:
                s += 1
                if s == k:
                    res += 1
                    m = {}
                    s = 0
                else:
                    m[n] = 1
        return res + 1