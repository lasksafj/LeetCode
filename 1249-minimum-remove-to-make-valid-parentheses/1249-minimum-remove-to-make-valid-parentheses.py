class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        n = 0
        for ch in s:
            if ch == '(':
                n += 1
                res.append(ch)
            elif ch == ')':
                if n > 0:
                    n -= 1
                    res.append(')')
            else:
                res.append(ch)
        i = len(res)-1
        while i >= 0:
            if n == 0:
                return ''.join(res)
            if res[i] == '(':
                res = res[:i] + res[i+1:]
                n -= 1
            i -= 1
        return ''