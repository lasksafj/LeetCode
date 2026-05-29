class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        T = {}
        mi = inf
        mi_i = -1
        for i,word in enumerate(wordsContainer):
            word = word[::-1]
            l = len(word)
            if l < mi:
                mi = l
                mi_i = i
            cur = T
            for w in word:
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]
                if 'len' not in cur:
                    cur['len'] = l
                if 'ans' not in cur:
                    cur['ans'] = i
                    continue
                if cur['len'] > l:
                    cur['ans'] = i
                    cur['len'] = l
        T['ans'] = mi_i
        res = []
        for word in wordsQuery:
            word = word[::-1]
            cur = T
            for w in word + '#':
                if w not in cur:
                    res.append(cur['ans'])
                    break
                cur = cur[w]
        return res