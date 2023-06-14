class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = sorted(Counter(nums).keys())
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
        l,r = 0, len(A)-1
        while l <= r:
            m = (l+r)//2
            if check(A[m],k):
                r = m-1
            else:
                l = m+1
        return A[l]