class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()
        res = 0
        j = 0
        for i in range(len(nums)):
            while min_dq and min_dq[-1] > nums[i]:
                min_dq.pop()
            while max_dq and max_dq[-1] < nums[i]:
                max_dq.pop()
            min_dq.append(nums[i])
            max_dq.append(nums[i])
            while j < i and max_dq[0] - min_dq[0] > limit:
                if max_dq[0] == nums[j]:
                    max_dq.popleft()
                if min_dq[0] == nums[j]:
                    min_dq.popleft()
                j += 1
            res = max(res, i-j+1)
        return res