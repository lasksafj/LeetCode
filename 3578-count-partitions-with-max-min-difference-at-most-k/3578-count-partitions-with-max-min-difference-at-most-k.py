class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N = len(nums) + 1
        nums = [0] + nums
        j = 1
        dp = [0]*N
        dp[0] = 1
        pre_dp = [1]*N
        A = SortedList()
        for i in range(1, N):
            A.add(nums[i])
            while A[-1] - A[0] > k:
                A.remove(nums[j])
                j += 1
            dp[i] = pre_dp[i-1] - (pre_dp[j-2] if j-2>=0 else 0)
            pre_dp[i] = pre_dp[i-1] + dp[i]
        return dp[-1] % (10**9+7)