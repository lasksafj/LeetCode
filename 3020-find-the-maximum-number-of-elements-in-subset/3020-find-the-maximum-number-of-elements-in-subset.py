class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        mp = Counter(nums)
        res = 1
        if 1 in mp:
            res = (mp[1]-1)//2 * 2 + 1
        del mp[1]
        dp = defaultdict(int)
        
        for n in sorted(mp)[::-1]:
            dp[n] = 1
            if mp[n] > 1 and n*n in dp:
                dp[n] = dp[n*n]+1
                res = max(res, dp[n]*2-1)
        return res