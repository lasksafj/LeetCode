class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        A,B = {},{}
        for i in range(n):
            c = s[i]
            if c not in A:
                A[c] = i
        for i in range(n-1,-1,-1):
            c = s[i]
            if c not in B:
                B[c] = i
        C = []
        for c in set(s):
            l = i = A[c]
            r = B[c]
            while i <= r:
                if l <= A[s[i]] and B[s[i]] <= r:
                    i += 1
                else:
                    r = max(r, B[s[i]])
                    l = min(l, A[s[i]])
                    i = l+1
            C.append([r-l+1, l, r])
        C.sort(key=lambda x: [x[2], x[0]])
        
        e = -1
        res = []
        for _,l,r in C:
            if l > e:
                res.append(s[l:r+1])
                e = r
        return res