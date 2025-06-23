class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def f(n):
            res = ''
            while n:
                res += str(n%k)
                n //= k
            return res == res[::-1]
        res = 0
        l = 0
        cnt = 0
        while cnt < n:
            for odd in [1,0]:
                for a in range(10**l, 10**(l+1)):
                    a = str(a)
                    b = int(a + a[::-1][odd:])
                    if f(b):
                        res += b
                        cnt += 1
                        if cnt == n:
                            return res
            l += 1
        return res