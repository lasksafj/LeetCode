class Solution:
    def countOfAtoms(self, f: str) -> str:
        a = []
        m = defaultdict(int)
        n = len(f)
        d = 1
        i = n-1
        while i >= 0:
            if f[i] == '(':
                d //= a[-1]
                a.pop()
            elif f[i] == ')':
                a.append(1)
            else:
                num = 1
                if f[i].isdigit():
                    j = i
                    while f[i].isdigit():
                        i -= 1
                    num = int(f[i+1:j+1])
                    if f[i] == ')':
                        a.append(num)
                        d *= num
                        num = 1
                j = i
                while f[i].islower():
                    i -= 1
                if f[i].isupper():
                    atom = str(f[i:j+1])
                    m[atom] += d*num
            i -= 1
        res = []
        for k,v in sorted(m.items()):
            res.append(k)
            if v > 1:
                res.append(str(v))
        return ''.join(res)