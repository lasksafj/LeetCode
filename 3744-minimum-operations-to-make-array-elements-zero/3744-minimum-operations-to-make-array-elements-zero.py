class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l,r in queries:
            a = 1
            op = 0
            d = 0
            while 1:
                if a > l:
                    op += (a-l) * d
                    l = a
                if a > r:
                    break
                a *= 4
                d += 1
            op += (r - l + 1) * d
            res += ceil(op/2)
        return res
