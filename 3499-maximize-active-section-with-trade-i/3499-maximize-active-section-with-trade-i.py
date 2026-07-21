class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        N = len(s)
        i = 0
        A = [-1]*3
        k = 0
        res = no1 = s.count('1')
        while i < N:
            j = i
            while j < N and s[j] == s[i]:
                j += 1
            A[k%3] = j-i
            if s[i] == '0' and -1 not in A:
                res = max(res, no1 + sum(A) - A[(k-1+3)%3])
            k += 1
            i = j
        return res