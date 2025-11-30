class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        m = s%p
        if m == 0: return 0
        cur = 0
        res = len(nums)
        mp = defaultdict(lambda: -inf)
        mp[0] = -1
        for i,n in enumerate(nums):
            cur += n
            res = min(res, i - mp[(cur%p - m + p)%p])
            mp[cur%p] = i
        return res if res < len(nums) else -1