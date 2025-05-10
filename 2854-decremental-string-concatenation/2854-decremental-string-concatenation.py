class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @cache
        def dfs(i, pl, pr):
            if i == len(words):
                return 0
            l,r = words[i][0], words[i][-1]
            return min(dfs(i+1, l, pr) - (pl == r), dfs(i+1, pl, r) - (pr == l))
        return sum(len(w) for w in words) + dfs(1, words[0][0], words[0][-1])