class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        i = 0
        N = len(s)
        A = []
        while i < N:
            j = i+1
            while j < N and s[j] == s[i]:
                j += 1
            A.append([s[i], j-i])
            i = j
        s = sum(l for a,l in A if a == '1')
        res = s
        for i,(a,l) in enumerate(A):
            if a == '0' and i >= 2:
                d = l + A[i-1][1] + A[i-2][1]
                res = max(res, s - A[i-1][1] + d)
        return res