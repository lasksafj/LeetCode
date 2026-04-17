class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        res = inf
        prev = {}
        for i,a in enumerate(nums[::-1]):
            ra = int(str(a)[::-1])
            res = min(res, i-prev.get(ra, -inf))
            prev[a] = i
        return res if res < inf else -1