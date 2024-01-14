class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def check(n):
            l = len(bin(n)[2:])
            # print(l)
            res = 0
            for i in range(l,0,-1):
                if i%x == 0:
                    a = (n+1) // pow(2,i)
                    res += a * pow(2,i-1) + max(0, n+1 - a * pow(2,i) - pow(2,i-1))
                    # print(i,res)
            # print('res',res)
            return res
        # check(9)
        l,r = 0,10**15
        while l <= r:
            mi = (l+r)//2
            # print(mi, check(mi))
            if check(mi) <= k:
                l = mi+1
            else:
                r = mi-1
        return r