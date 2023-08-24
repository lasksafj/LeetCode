class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = ''
        A = []
        L = 0
        res = []
        for w in words:
            L += len(w) + 1
            A.append(w)
            if L-1 > maxWidth:
                L -= len(A.pop()) + 2
                if len(A) > 1:
                    d1 = (maxWidth - L) // (len(A)-1)
                    d2 = (maxWidth - L) % (len(A)-1)
                    for a in A[:-1]:
                        line += a + (' ' * (d1+1 + (d2 > 0)))
                        d2 -= 1
                    line += A[-1]
                else:
                    line += A[0] + (' ' * (maxWidth - len(A[0])))
                res.append(line)
                A = [w]
                line = ''
                L = len(w) + 1
        for a in A[:-1]:
            line += a + ' '
        line += A[-1]
        if line != '':
            line += ' ' * (maxWidth - len(line))
            res.append(line)
        return res