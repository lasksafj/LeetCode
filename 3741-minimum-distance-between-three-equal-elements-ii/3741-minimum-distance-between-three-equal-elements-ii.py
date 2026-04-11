class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = inf
        mp = defaultdict(list)
        for i,n in enumerate(nums):
            mp[n].append(i)
            A = mp[n]
            if len(A) >= 3:
                res = min(res, (A[-1]-A[-3])*2)
        return res if res < inf else -1