class Solution:
    def longestDupSubstring(self, s: str) -> str:
        A = [ord(ch) - ord('a') for ch in s]
        mod = 10**11 + 7
        def RK(x):
            if x == 0:
                return True
            m = defaultdict(list)
            px = pow(26,x,mod)
            cur = 0
            for i in range(x):
                cur = (cur*26 + A[i]) % mod
            m[cur].append(0)
            for i in range(x, len(A)):
                cur = (cur*26 + A[i] - A[i-x]*px) % mod
                # print(i, m[cur])
                for j in m[cur]:
                    if A[i-x+1:i+1] == A[j:j+x]:
                        return i-x+1
                m[cur].append(i-x+1)
            return -1
        l,r = 0,len(A)-1
        # print(RK(2))
        res = 0
        while l <= r:
            mi = (l+r)//2
            # print(mi,RK(mi))
            start = RK(mi)
            if start > -1:
                l = mi+1
                res = start
            else:
                r = mi-1
        return s[res:res+r] if r > -1 else ''