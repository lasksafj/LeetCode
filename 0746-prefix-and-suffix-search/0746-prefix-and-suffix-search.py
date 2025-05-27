class WordFilter:

    def __init__(self, words: List[str]):
        self.T = {}
        def add(w, i):
            cur = self.T
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                cur['#'] = i
        for i,w in enumerate(words):
            for j in range(len(w)):
                add(w[j:] + '$' + w, i)


    def f(self, pref: str, suff: str) -> int:
        s = suff + '$' + pref
        cur = self.T
        for c in s:
            if c not in cur:
                return -1
            cur = cur[c]
        return cur['#']


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)