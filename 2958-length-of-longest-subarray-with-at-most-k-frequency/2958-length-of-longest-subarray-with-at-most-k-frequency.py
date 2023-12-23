class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        j = 0
        m = defaultdict(int)
        for i in range(len(nums)):
            m[nums[i]] += 1
            while m[nums[i]] > k:
                m[nums[j]] -= 1
                j += 1
            res = max(res, i-j+1)
        return res