class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        T = {}
        for w in dictionary:
            cur = T
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['end'] = True
        res = []
        # print(T)
        for w in sentence.split(' '):
            cur = T
            a = ''
            # print(w)
            for c in w + '-':
                if 'end' in cur:
                    # print('end in cur')
                    res.append(a)
                    break
                if c not in cur:
                    # print('c not in cur')
                    res.append(w)
                    break
                a += c
                cur = cur[c]
        
        return ' '.join(res)