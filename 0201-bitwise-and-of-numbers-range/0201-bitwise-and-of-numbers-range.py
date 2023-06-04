class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        a = bin(left)
        b = bin(right)
        if len(b) > len(a):
            return 0
        i = 2
        res = 0
        while i < len(a) and a[i] == b[i]:
            res = res<<1 | int(a[i])
            i += 1
        return res << (len(a)-i)