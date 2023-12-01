class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        N = len(nums)
        dq = deque([(0,0,0)]) #s+last,s,dp
        s = 0
        for i in range(N):
            s += nums[i]
            while dq and dq[0][0] <= s:
                _,pre_s,pre_dp = dq.popleft()
            s_last = s + (s - pre_s)
            while dq and dq[-1][0] >= s_last:
                dq.pop()
            dq.append((s_last, s, pre_dp+1))
        return dq[-1][2]