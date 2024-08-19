fmin = lambda x, y: x if x < y else y
fmax = lambda x, y: x if x > y else y
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        A = [-1] + [i for i in range(N) if s[i] == '0'] + [N]
        res = 0
        j = 0
        ma = isqrt(N)+1
        for i,ch in enumerate(s):
            for z in range(ma):
                if j+z >= len(A)-1:
                    break
                r = fmax(i,A[j+z])
                a = fmax(0, z*z+z - (r-i+1))
                res += fmax(0, A[j+z+1] - fmax(i, A[j+z]) - a)
            if ch == '0':
                j += 1
        return res