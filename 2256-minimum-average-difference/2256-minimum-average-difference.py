class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        post = [0]*n
        post[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            post[i] = post[i+1] + nums[i]
        left = 0
        res = 0
        avgdif = inf
        for i in range(n):
            left += nums[i]
            a = abs(left//(i+1) - ((post[i+1]//(n-i-1)) if i+1<n else 0))
            if avgdif > a:
                avgdif = a
                res = i
        return res
        