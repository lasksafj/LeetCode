class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        A = zip(words, groups)
        res = []
        prev = -1
        for w,g in A:
            if g != prev:
                res.append(w)
                prev = g
        return res