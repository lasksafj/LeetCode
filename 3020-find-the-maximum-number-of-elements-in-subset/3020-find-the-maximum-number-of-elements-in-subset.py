class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort()
        cnt = Counter(nums)
        vis = set()
        res = 1
        if 1 in cnt:
            res = cnt[1] - (cnt[1]%2 == 0)
        for n in nums:
            if n in vis or n == 1:
                continue
            l = 0
            x = n
            while cnt[x] >= 2:
                vis.add(x)
                x = x**2
                l += 1
            if x in cnt:
                res = max(res, l*2+1)
            else:
                res = max(res, (l-1)*2+1)
        return res