class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        m,n = len(pattern),len(s)
        if m != n:
            return False
        mp = {}
        ms = {}
        for i in range(m):
            if pattern[i] in mp and mp[pattern[i]] != s[i]\
                or s[i] in ms and ms[s[i]] != pattern[i]:
                return False
            mp[pattern[i]] = s[i]
            ms[s[i]] = pattern[i]
        return True