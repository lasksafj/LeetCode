class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[defaultdict(int) for _ in range(3)] for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                for k in range(3):
                    if k < 2:
                        dp[i][k+1][diff] += dp[j][k][diff] + (1 if k==0 else 0)
                    else:
                        dp[i][k][diff] += dp[j][k][diff]
                # print(dp[i][2][diff])
                # res += dp[i][2][diff]
            # print(dp[i][2])
            for e,v in dp[i][2].items():
                res += v
        return res