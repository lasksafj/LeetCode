class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        pre = [0]*N
        pre[0] = (customers[0] == 'N')
        for i in range(1,N):
            pre[i] = pre[i-1] + (customers[i] == 'N')
        p = 0
        pen = pre[-1]
        res = N
        for i in range(N-1, -1, -1):
            p += (customers[i] == 'Y')
            if (pre[i-1] if i>0 else 0) + p <= pen:
                pen = pre[i-1] + p
                res = i
        return res