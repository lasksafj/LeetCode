class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        mod = 10**9+7
        for i in range(2,n+1):
            a = 2*(i-1)+1
            res = res * (a*(a+1)//2) % mod
        return res