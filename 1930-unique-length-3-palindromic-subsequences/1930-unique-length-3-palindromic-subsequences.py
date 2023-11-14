class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        last = defaultdict(int)
        for i,c in enumerate(s):
            last[c] = i
        mp = {}
        res = 0
        for i,c in enumerate(s):
            for a in list(mp.keys()):
                if c == a and last[c] == i:
                    res += len(mp[a])
                    del mp[a]
                else:
                    mp[a].add(c)
            if c not in mp:
                mp[c] = set()
        return res