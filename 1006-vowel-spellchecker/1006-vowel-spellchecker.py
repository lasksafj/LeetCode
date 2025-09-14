class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        mp = {}
        for i,w in enumerate(wordlist):
            if w.lower() not in mp:
                mp[w.lower()] = w
            nw = ''.join('*' if c in 'aeiou' else c for c in w.lower())
            if nw not in mp:
                mp[nw] = w
        wordlist = set(wordlist)
        res = []
        for w in queries:
            if w in wordlist:
                res.append(w)
                continue
            w = w.lower()
            if w in mp:
                res.append(mp[w])
                continue
            nw = ''.join('*' if c in 'aeiou' else c for c in w.lower())
            if nw in mp:
                res.append(mp[nw])
                continue
            res.append('')
        return res