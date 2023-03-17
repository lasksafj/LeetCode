class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [0] * n
        c = 0
        for i in range(n):
            if s[i]:
                continue
            c += 1
            s[i] = c
            if c > 26:
                return ''
            for j in range(i+1, n):
                if lcp[i][j] > 0:
                    if s[j]:
                        return ''
                    s[j] = s[i]
        # print(s)
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == s[j]:
                    a = lcp[i+1][j+1] if i+1 < n and j+1 < n else 0
                    if lcp[i][j] != a + 1:
                        return ''
                elif lcp[i][j] > 0:
                    return ''
        
        return ''.join([chr(c+96) for c in s])