class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            mp = {}
            unique = 0
            ma = 0
            for j in range(i, len(s)):
                if s[j] not in mp:
                    unique += 1
                    mp[s[j]] = 1
                else:
                    mp[s[j]] += 1
                ma = max(ma, mp[s[j]])
                if unique*ma == j-i+1:
                    res = max(res, j-i+1)
        return res