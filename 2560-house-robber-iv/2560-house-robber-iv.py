class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def check(x, k):
            i = 0
            while i < n:
                if nums[i] <= x:
                    i += 2
                    k -= 1
                    if k == 0:
                        return True
                else:
                    i += 1
            return False
        l,r = min(nums),max(nums)
        while l <= r:
            m = (l+r)//2
            if check(m,k):
                r = m-1
            else:
                l = m+1
        return l