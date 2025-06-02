class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for a,b in queries:
            c = 1
            d = 0
            op = 0
            while c <= b:
                op += max(0, c-a) * d
                if max(a,c) <= b:
                    a = max(a,c)
                c *= 4
                d += 1
            op += (b-a+1)*d
            res += ceil(op/2)
        return res