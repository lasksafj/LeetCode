class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                a = 0
                if diff not in dp[j]:
                    if diff in dp[i]:
                        dp[i][diff] += 1
                    else:
                        dp[i][diff] = 1
                else:
                    a = dp[j][diff]
                    if diff in dp[i]:
                        dp[i][diff] += dp[j][diff] + 1
                    else:
                        dp[i][diff] = dp[j][diff] + 1
                    
                res += a
        return res