class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N = len(nums) + 1
        nums = [0] + nums
        j = 1
        dp = [0]*N
        dp[0] = 1
        pre_dp = [1]*N
        qmax = deque()
        qmin = deque()
        for i in range(1, N):
            while qmax and nums[qmax[-1]] < nums[i]:
                qmax.pop()
            qmax.append(i)
            while qmin and nums[qmin[-1]] > nums[i]:
                qmin.pop()
            qmin.append(i)
            while nums[qmax[0]] - nums[qmin[0]] > k:
                j += 1
                if qmax[0] < j:
                    qmax.popleft()
                if qmin[0] < j:
                    qmin.popleft()
                
            dp[i] = pre_dp[i-1] - (pre_dp[j-2] if j-2>=0 else 0)
            pre_dp[i] = pre_dp[i-1] + dp[i]
        return dp[-1] % (10**9+7)