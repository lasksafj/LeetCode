class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def sol(cur, n):
            if len(path) == 4:
                if cur == len(s):
                    res.append('.'.join([str(i) for i in path]))
                return
            if cur == len(s):
                return
            if n == 0 and s[cur] == '0':
                path.append(n)
                sol(cur+1, 0)
                path.pop()
                return
            n = n*10 + int(s[cur])
            if n >= 0 and n <= 255:
                path.append(n)
                sol(cur+1, 0)
                path.pop()
            sol(cur+1, n)
        res = []
        path = []
        sol(0,0)
        return res