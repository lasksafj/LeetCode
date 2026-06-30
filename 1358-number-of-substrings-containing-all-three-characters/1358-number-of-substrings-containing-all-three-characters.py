class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp = defaultdict(int)
        j = 0
        res = 0
        for i in range(len(s)):
            mp[s[i]] += 1
            while j < i and mp[s[j]] > 1:
                mp[s[j]] -= 1
                j += 1
            if len(mp) == 3:
                res += j+1
        return res