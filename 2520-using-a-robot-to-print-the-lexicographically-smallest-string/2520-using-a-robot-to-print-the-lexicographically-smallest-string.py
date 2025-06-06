class Solution:
    def robotWithString(self, s: str) -> str:
        N = len(s)
        mi = '|'
        j = N
        ne = [-1]*N
        for i in range(N-1, -1, -1):
            if s[i] <= mi:
                mi = s[i]
                j = i
            ne[i] = j

        i = 0
        res = ''
        q = ''
        while i < N:
            j = ne[i]
            # print(s[j], q)
            if not q or s[j] < q[-1]:
                q += s[i:j]
                res += s[j]
                i = j+1
            else:
                res += q[-1]
                q = q[:-1]
        return res + q[::-1]