class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        a = 0
        for row in bank:
            if int(row,2) == 0:
                continue
            b = row.count('1')
            res += a*b
            a = b
        return res