class Solution:
    def minimumTime(self, s: str) -> int:
        N = len(s)
        i,j = 0,N-1
        res = 0
        
        while i < N and s[i] == '1':
            res += 1
            i += 1
        while j > i and s[j] == '1':
            res += 1
            j -= 1
        A = []
        for k in range(i,j+1):
            A.append(int(s[k]=='1'))
        N = len(A)
        ss = sum(A)
        cur = ss
        B = [cur*2]
        mi = cur*2
        for i in range(1,N):
            cur -= A[i-1]
            mi = min(mi, cur*2+i)
            B.append(mi)
        # print(B)
        cur = ss
        mi = cur*2
        rem = ss*2
        for j in range(N-1,-1,-1):
            cur -= A[j]
            mi = min(mi, cur*2+N-j)
            rem = min(rem, B[j]+mi-ss*2)
        
        return res+rem