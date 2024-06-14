class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        mp = Counter(nums)
        res = 0
        free = min(mp)
        for i in sorted(mp):
            while mp[i] > 1:
                free = max(i+1, free)
                while mp[free] > 0:
                    free += 1
                mp[i] -= 1
                mp[free] = 1
                res += free-i
        return res