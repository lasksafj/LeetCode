class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        neg = 0
        ma_neg = -inf
        mi_pos = inf
        for row in matrix:
            for n in row:
                if n <= 0:
                    neg += 1
                    ma_neg = max(ma_neg, n)
                else:
                    mi_pos = min(mi_pos, n)
                res += abs(n)
        if neg%2 == 0:
            return res
        if -ma_neg > mi_pos:
            return res - 2*mi_pos
        return res + 2*ma_neg