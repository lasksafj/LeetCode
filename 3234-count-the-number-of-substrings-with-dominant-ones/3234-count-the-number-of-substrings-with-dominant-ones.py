class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        A = [-1]
        for i,ch in enumerate(s):
            if ch == '0':
                A.append(i)
        A.append(len(s)-1)
        def F(x):
            i = 0
            res = 0
            no0 = 0
            l = 0
            for r in range(len(s)):
                no0 += s[r]=='0'
                if no0 > x:
                    i += 1
                    l = A[i]+1
                    no0 -= 1
                if no0 == x:
                    a = no0
                    while a==x and l<=r and l <= A[i+1] and a**2 <= r-l+1 - a:
                        a -= s[l]=='0'
                        l += 1
                    if i < len(A) and l-1 <= r and A[i]<l:
                        res += l-A[i]-1
                        # print('--',l,r,A[i],'--',res)


            # print(x,res)
            return res
        res = 0
        x = 0
        while x**2+x <= len(s):
            res += F(x)
            x += 1
        # print()
        return res