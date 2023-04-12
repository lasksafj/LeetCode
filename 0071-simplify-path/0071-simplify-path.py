class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        res = []
        for p in path:
            if p == '..' :
                if res:
                    res.pop()
            elif p != '' and p != '.':
                res.append(p)
        return '/' + '/'.join(res)