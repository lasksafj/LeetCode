class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        m = defaultdict(int)
        for w in words:
            for ch in w:
                m[ch] += 1
        for ch in m:
            if m[ch] % len(words):
                return False
        return True