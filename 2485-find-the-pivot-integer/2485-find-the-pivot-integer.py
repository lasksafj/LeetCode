class Solution:
    def pivotInteger(self, n: int) -> int:
        s = sum(list(range(n+1)))
        cur = 0
        for i in range(1,n+1):
            cur += i
            if cur == s:
                return i
            s -= i
        return -1