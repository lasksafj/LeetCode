class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt1 = 0
        cnt2 = 0
        for n in nums:
            cur = 0
            while n > 0:
                if n&1:
                    n -= 1
                    cnt1 += 1
                else:
                    n //= 2
                    cur += 1
            cnt2 = max(cnt2, cur)
        
        def check(mi):
            return cnt1+cnt2 <= mi
            
        l,r = 0,10**9
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l