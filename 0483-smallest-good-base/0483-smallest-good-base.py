class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def check(k, p):
            a = 0
            i = 0
            while i < p:
                a += k**i
                i += 1
            return a
        
        n = int(n)
        max_m = int(math.log(n,2))
        for i in range(max_m+1,0,-1):
            l,r = 2,n
            while l <= r:
                m = (l+r)//2
                y = check(m, i)
                if y < n:
                    l = m+1
                elif y > n:
                    r = m-1
                else:
                    return str(m)
        return str(r)