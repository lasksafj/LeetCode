class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        A = []
        for i in range(len(nums)-1):
            A.append(nums[i+1]-nums[i])
        # A.sort()
        # print(A)
        def check(x):
            cnt = 0
            i = 0
            while i < len(A):
                if A[i] <= x:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= p
        l,r = 0,max(A)
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l