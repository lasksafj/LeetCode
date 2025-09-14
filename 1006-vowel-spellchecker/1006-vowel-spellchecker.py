class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        mp = {}
        for i,w in enumerate(wordlist):
            if w.lower() not in mp:
                mp[w.lower()] = [w,i]
        wordlist = set(wordlist)
        res = []
        for w in queries:
            if w in wordlist:
                res.append(w)
                continue
            w = w.lower()
            if w in mp:
                res.append(mp[w][0])
                continue
            
            vow_cnt = len([c for c in w if c in 'aeiou'])
            cur = ''
            cur_p = inf
            for vows in product('aeiou', repeat=vow_cnt):
                A = list(w)
                j = 0
                for i,c in enumerate(A):
                    if c in 'aeiou':
                        A[i] = vows[j]
                        j += 1
                tmp = ''.join(A)
                if tmp in mp and cur_p > mp[tmp][1]:
                    cur_p = mp[tmp][1]
                    cur = mp[tmp][0]
            
            res.append(cur)
        return res