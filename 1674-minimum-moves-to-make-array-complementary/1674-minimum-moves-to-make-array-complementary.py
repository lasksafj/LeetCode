class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        mp = defaultdict(int)
        for i in range(N//2):
            a,b = nums[i], nums[N-i-1]
            if a>b: a,b = b,a
            l = a+1
            r = limit+b
            mi = a+b
            mp[0] += 2
            mp[l] -= 2
            mp[l] += 1
            mp[mi] -= 1
            mp[mi+1] += 1
            mp[r+1] -= 1
            mp[r+1] += 2
        cur = 0
        res = inf
        for k in sorted(mp.keys()):
            cur += mp[k]
            res = min(res, cur)
        return res