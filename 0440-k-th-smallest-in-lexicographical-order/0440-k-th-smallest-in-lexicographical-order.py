class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(cur):
            res = 1
            d = 1
            while cur*10 <= n:
                d *= 10
                cur *= 10
                res += min(d, n-cur+1)
            return res
        cur = 1
        k -= 1
        while k:
            a = count(cur)
            if a <= k:
                k -= a
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur