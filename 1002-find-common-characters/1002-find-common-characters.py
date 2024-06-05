class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = [{} for _ in range(len(words))]
        for i,w in enumerate(words):
            cnt[i] = Counter(w)
        res = []
        for ch in ascii_lowercase:
            res += [ch] * min(cnt[i][ch] for i in range(len(words)))
        return res