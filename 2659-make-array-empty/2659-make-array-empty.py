class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        p = sorted(list(range(n)), key=lambda i:nums[i])
        t = [0]*(n+1)
        
        def update(i,v):
            i += 1
            while i <= n:
                t[i] += v
                i += i&(-i)
        def getsum(i):
            i += 1
            res = 0
            while i > 0:
                res += t[i]
                i -= i&(-i)
            return res
        
        for i in range(n):
            update(i,1)
        res = 0
        cur = 0
        a = 1
        # print(p)
        for i in p:
            if i >= cur:
                res += getsum(i) - getsum(cur) + a
            else:
                res += getsum(n-1) - getsum(cur) + getsum(i)
            cur = i
            # print(getsum(i),getsum(cur),getsum(n-1))
            update(i, -1)
            # print(res)
            a = 0
        return res
            