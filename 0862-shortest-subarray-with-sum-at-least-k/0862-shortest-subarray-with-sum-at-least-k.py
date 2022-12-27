class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n+1)
        pre[0] = nums[0]
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        dq = deque([0])
        res = inf
        for i in range(n+1):
            while dq and pre[i] - pre[dq[0]] >= k:
                res = min(res, i - dq.popleft())
            while dq and pre[dq[-1]] > pre[i]:
                dq.pop()
            dq.append(i)
        return res if res < inf else -1