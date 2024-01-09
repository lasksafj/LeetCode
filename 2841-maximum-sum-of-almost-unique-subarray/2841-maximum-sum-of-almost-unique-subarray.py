class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        mp = defaultdict(int)
        s = 0
        res = 0
        for i in range(k):
            mp[nums[i]] += 1
            s += nums[i]
        if len(mp) >= m:
            res = max(res, s)
        j = 0
        for i in range(k,len(nums)):
            s += nums[i]
            mp[nums[i]] += 1
            s -= nums[j]
            mp[nums[j]] -= 1
            if mp[nums[j]] == 0:
                del mp[nums[j]]
            j += 1
            if len(mp) >= m:
                res = max(res, s)
        return res