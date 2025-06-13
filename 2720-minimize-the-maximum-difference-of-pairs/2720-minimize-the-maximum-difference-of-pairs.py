class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        N = len(nums)
        A = [b-a for a,b in pairwise(nums)]
        def check(mi):
            res = i = 0
            while i < len(A):
                if A[i] <= mi:
                    res += 1
                    i += 2
                else:
                    i += 1
            return res >= p
        l,r = 0, nums[-1] - nums[0]
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l