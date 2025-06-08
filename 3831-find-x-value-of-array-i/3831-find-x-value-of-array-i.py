class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        dp = [[0]*(N+1) for _ in range(k)]
        for i in range(1, N+1):
            a = nums[i-1]
            for m in range(k):
                dp[(m*a)%k][i] += dp[m][i-1]
            dp[a%k][i] += 1
        return [sum(row) for row in dp]