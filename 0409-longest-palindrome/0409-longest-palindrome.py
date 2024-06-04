class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = defaultdict(int)
        res = 0
        for ch in s:
            mp[ch] += 1
            if mp[ch] == 2:
                res += 2
                del mp[ch]
        return res + (len(mp)>0)