class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        default_i = 0
        mi = inf
        for i,word in enumerate(wordsContainer):
            if len(word) < mi:
                default_i = i
                mi = len(word)
        
        root = {}
        def add(i, word, root):
            root['idx'] = default_i
            for ch in word:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]
                if 'min_len' not in root or root['min_len'] > len(word):
                    root['min_len'] = len(word)
                    root['idx'] = i
        
        for i,word in enumerate(wordsContainer):
            word = word[::-1]
            add(i, word, root)
        res = []
        for word in wordsQuery:
            word = word[::-1]
            cur = root
            added = False
            for ch in word:
                if ch in cur:
                    cur = cur[ch]
                else:
                    res.append(cur['idx'])
                    added = True
                    break
            if not added:
                res.append(cur['idx'])
                    
        return res