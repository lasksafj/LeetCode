class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        res = [1]*len(nums)
        # res[0] = 1
        for i in range(len(nums)):
            ma = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] > ma:
                        dp[i] = dp[j]+1
                        res[i] = res[j]
                        ma = dp[j]
                    elif dp[j] == ma:
                        res[i] += res[j]
            # print(res, dp)
        ma = max(dp)
        return sum(a for i,a in enumerate(res) if dp[i] == ma)