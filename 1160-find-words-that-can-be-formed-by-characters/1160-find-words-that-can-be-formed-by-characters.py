class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        mp = Counter(chars)
        res = 0
        for w in words:
            a = mp.copy()
            good = True
            for ch in w:
                a[ch] -= 1
                if a[ch] < 0:
                    good = False
                    break
            if good:
                res += len(w)
        return res