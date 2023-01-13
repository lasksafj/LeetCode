class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def check(k, p):
            a = 0
            i = 0
            while i < p:
                a += k**i
                i += 1
            if a < n:
                return -1
            elif a > n:
                return 1
            else:
                return 0
        
        n = int(n)
        max_m = int(math.log(n,2))
        for i in range(max_m+1,0,-1):
            l,r = 2,n
            while l <= r:
                m = (l+r)//2
                y = check(m, i)
                if y == -1:
                    l = m+1
                elif y == 1:
                    r = m-1
                else:
                    return str(m)
        return str(r)