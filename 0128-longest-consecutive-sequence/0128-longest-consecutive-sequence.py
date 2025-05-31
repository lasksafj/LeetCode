class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n not in s: continue
            d = n+1
            cnt = 1
            while d in s:
                s.remove(d)
                d += 1
                cnt += 1
            d = n-1
            while d in s:
                s.remove(d)
                d -= 1
                cnt += 1
            res = max(res, cnt)
        return res