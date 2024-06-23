class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        res = -inf
        for i,n in enumerate(nums):
            if dq and i - dq[0][1] > k:
                dq.popleft()
            s = n + (dq[0][0] if dq else 0)
            res = max(res, s)
            while dq and dq[-1][0] < s:
                dq.pop()
            if s > 0:
                dq.append([s,i])
        return res