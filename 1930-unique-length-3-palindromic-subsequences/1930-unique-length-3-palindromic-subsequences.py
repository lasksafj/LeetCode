class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        last = [-1]*26
        first = [-1]*26
        for i,c in enumerate(s):
            a = ord(c) - ord('a')
            last[a] = i
            if first[a] == -1:
                first[a] = i
        res = 0
        for c in string.ascii_lowercase:
            a = ord(c) - ord('a')
            i = first[a]
            j = last[a]
            if -1 < i < j:
                between = set()
                for k in range(i+1,j):
                    between.add(s[k])
                res += len(between)
        return res