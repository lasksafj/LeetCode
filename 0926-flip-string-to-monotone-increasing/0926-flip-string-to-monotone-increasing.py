class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res,no1 = 0,0
        for c in s:
            if c == '0':
                res = min(no1, res+1)
            else:
                no1 += 1
        return res