class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = -inf
        cur = 0
        mp = {}
        for n in nums:
            cur += n
            if n-k in mp:
                res = max(res, cur - mp[n-k])
            if n+k in mp:
                res = max(res, cur - mp[n+k])
            if n in mp:
                mp[n] = min(mp[n], cur-n)
            else:
                mp[n] = cur-n
        return res if res > -inf else 0