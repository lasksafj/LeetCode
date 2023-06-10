class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def cal(a,noe):
            s = 0
            if a - (noe-1) > 0:
                s = (a + (a - (noe-1))) * noe // 2
            else:
                s = (a + 1) * a // 2 + noe - a
            return s
        
        def check(x):
            s = cal(x-1, index) + cal(x, n-index)
            return s <= maxSum
        
        l,r = 1,maxSum
        while l <= r:
            m = (l+r)//2
            if check(m):
                l = m+1
            else:
                r = m-1
        return r
            
        