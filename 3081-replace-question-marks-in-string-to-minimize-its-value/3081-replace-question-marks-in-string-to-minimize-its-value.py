from sortedcontainers import SortedList
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        L = [0]*26
        R = [[0]*26 for _ in range(len(s))]
        for ch in ascii_lowercase:
            for i in range(len(s)-1,0,-1):
                R[i-1][ord(ch)-ord('a')] = R[i][ord(ch)-ord('a')] + (s[i] == ch)
        i = 0
        res = []
        
        A = []
        while i < len(s):
            if s[i] == '?':
                mi = inf
                mi_idx = -1
                for j in range(26):
                    if L[j] + R[i][j] < mi:
                        mi = L[j] + R[i][j]
                        mi_idx = j
                L[mi_idx] += 1
                A.append(mi_idx)
            else:
                L[ord(s[i])-ord('a')] += 1
            i += 1
        A.sort()
        i = 0
        for ch in s:
            if ch == '?':
                res.append(chr(A[i]+ord('a')))
                i += 1
            else:
                res.append(ch)
        
        return ''.join(res)