class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        d = sum(nums)%p
        mp = defaultdict(int)
        pre = [0]*(len(nums)+1)
        mp[0] = 0
        res = inf
        for i in range(len(nums)):
            a = pre[i+1] = (pre[i]+nums[i])%p
            mp[a] = i+1
            if a-d in mp:
                res = min(res, i+1 - mp[a-d])
            if a+p-d in mp:
                res = min(res, i+1 - mp[a+p-d])
        return res if res < len(nums) else -1