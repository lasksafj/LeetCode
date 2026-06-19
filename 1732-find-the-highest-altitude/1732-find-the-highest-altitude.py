class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = 0
        res = 0
        for g in gain:
            a += g
            res = max(res, a)
        return res