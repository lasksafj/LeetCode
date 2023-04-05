class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(x):
            ne_num = nums[-1]
            for i in range(len(nums)-1,0,-1):
                if ne_num > x:
                    a = ne_num-x
                    ne_num = nums[i-1]+a
                else:
                    ne_num = nums[i-1]
            return ne_num <= x
        l,r = min(nums), max(nums)
        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m-1
            else:
                l = m+1
        return l