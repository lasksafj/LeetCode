class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        @cache
        def f(i):
            return (1 << (ord(s[i])-ord('a')) ^ f(parent[i])) if i else 0
        m = defaultdict(int)
        res = 0
        for i in range(len(s)):
            v = f(i)
            res += m[v]
            m[v] += 1
            for j in range(26):
                res += m[v ^ (1 << j)]
        return res