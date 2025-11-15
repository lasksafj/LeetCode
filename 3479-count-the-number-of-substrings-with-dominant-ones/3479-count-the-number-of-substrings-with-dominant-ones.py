class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        ne = [0]*N
        j = N
        for i in range(N-1, -1, -1):
            ne[i] = j
            if s[i] == '0':
                j = i
        res = 0
        for i in range(N):
            j = i
            n0 = s[i] == '0'
            while j < N and n0*n0 <= N:
                n1 = j-i+1 - n0
                nj = ne[j]
                res += max(0, nj-j - max(0, n0*n0 - n1))
                j = nj
                n0 += 1
        return res