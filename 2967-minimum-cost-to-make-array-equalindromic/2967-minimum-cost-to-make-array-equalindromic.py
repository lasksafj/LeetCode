class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        N = len(nums)
        med = (nums[(N-1)//2] + nums[N//2])//2
        med = str(med)
        l = len(med)
        xr = []

        x = int(med[:(l+1)//2])
        for a in [-1,0,1]:
            if x+a == 0:
                xr.append(9)
                continue
            y = str(x + a)
            if len(y) < len(str(x)):
                s = '9'*(l-1)
            else:
                s = y + (y[::-1][1:] if l%2 else y[::-1])

            xr.append(int(s))

        # print(med,xr)
        res = inf
        for i in xr:
            cur = 0
            for n in nums:
                cur += abs(n-i)
            res = min(res,cur)
        return res