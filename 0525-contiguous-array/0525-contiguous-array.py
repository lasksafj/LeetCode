class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        s = 0
        mp = {0:-1}
        for i,n in enumerate(nums):
            s += 1 if n else -1
            if s not in mp:
                mp[s] = i
            res = max(res, i-mp[s])
        return res