class Solution:
    def minimumTime(self, s: str) -> int:
        N = len(s)
        A = []
        for k in range(N):
            A.append(int(s[k]=='1'))
        ss = sum(A)
        cur = ss
        mi = cur*2
        B = [mi]
        for i in range(1,N):
            cur -= A[i-1]
            mi = min(mi, cur*2+i)
            B.append(mi)
        cur = ss
        mi = cur*2
        res = ss*2
        for j in range(N-1,-1,-1):
            cur -= A[j]
            mi = min(mi, cur*2+N-j)
            res = min(res, B[j]+mi-ss*2)
        
        return res