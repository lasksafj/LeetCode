class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        cur = 0
        res = -inf
        mp = defaultdict(lambda: inf)
        mp[0] = 0
        for i,n in enumerate(nums):
            i += 1
            cur += n
            res = max(res, cur - mp[i%k])
            mp[i%k] = min(mp[i%k], cur)
        return res