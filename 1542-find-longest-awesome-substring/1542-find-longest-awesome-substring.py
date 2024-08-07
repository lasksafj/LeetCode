class Solution:
    def longestAwesome(self, s: str) -> int:
        mp = defaultdict(lambda:inf)
        mp[0] = -1
        res = 0
        cur = 0
        for i in range(len(s)):
            n = 1<<int(s[i])
            cur ^= n
            for k in range(10):
                res = max(res, i-mp[cur^(1<<k)])
            res = max(res, i-mp[cur])
            mp[cur] = min(i, mp[cur])
        return res