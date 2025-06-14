class Solution:
    def minMaxDifference(self, num: int) -> int:
        mi,ma = inf,-inf
        for d in range(10):
            for nd in range(10):
                if d == nd: continue
                d,nd = str(d),str(nd)
                A = list(str(num))
                for i in range(len(A)):
                    if A[i] == d:
                        A[i] = nd
                x = int(''.join(A))
                ma = max(ma, x)
                mi = min(mi, x)
        return ma - mi