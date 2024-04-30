class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        mask = 0
        res = 0
        for w in word:
            i = ord(w)-ord('a')
            mask ^= 1<<i
            res += mp[mask]
            for j in range(10):
                res += mp[mask^(1<<j)]
            mp[mask] += 1
        return res