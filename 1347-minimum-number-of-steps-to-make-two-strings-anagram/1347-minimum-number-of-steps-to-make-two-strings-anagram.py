class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ms = Counter(s)
        mt = Counter(t)
        res = 0
        for ch,v in ms.items():
            if mt[ch] < v:
                res += v - mt[ch]
        return res