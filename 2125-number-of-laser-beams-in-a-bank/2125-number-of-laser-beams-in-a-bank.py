class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        res = 0
        for r in bank:
            d = r.count('1')
            if d > 0:
                res += prev*d
                prev = d
        return res