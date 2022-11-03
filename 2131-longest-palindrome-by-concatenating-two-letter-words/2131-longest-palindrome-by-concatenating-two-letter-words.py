class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = defaultdict(str)
        res = 0
        for w in words:
            tmp = w[::-1]
            if tmp in m and m[tmp] > 0:
                res += 2
                m[tmp] -= 1
            else:
                if w in m:
                    m[w] += 1
                else:
                    m[w] = 1
        for e in m:
            if e[0] == e[1] and m[e] == 1:
                res += 1
                break
        return res * 2