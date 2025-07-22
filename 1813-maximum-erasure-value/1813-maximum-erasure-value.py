class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = s = 0
        mp = defaultdict(int)
        j = 0
        for i in range(len(nums)):
            s += nums[i]
            mp[nums[i]] += 1
            while mp[nums[i]] > 1:
                s -= nums[j]
                mp[nums[j]] -= 1
                j += 1
            res = max(res, s)
        return res