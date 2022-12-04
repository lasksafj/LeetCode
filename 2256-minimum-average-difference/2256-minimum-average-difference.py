class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        left = 0
        res = 0
        avgdif = inf
        for i in range(n):
            left += nums[i]
            s -= nums[i]
            a = abs(left//(i+1) - ((s//(n-i-1)) if i+1<n else 0))
            if avgdif > a:
                avgdif = a
                res = i
        return res
        