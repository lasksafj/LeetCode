class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        f = list(range(n))
        r = [0]*n
        def root(x):
            if x == f[x]:
                return x
            return root(f[x])
        def union(a,b):
            a,b = root(a),root(b)
            if a == b:
                return
            if r[a] < r[b]:
                f[a] = b
            elif r[a] > r[b]:
                f[b] = a
            else:
                f[a] = b
                r[b] += 1
        res = []
        for a,b in requests:
            for x,y in restrictions:
                a,b,x,y = root(a),root(b),root(x),root(y)
                if (a == x and b == y) or (a == y and b == x):
                    res.append(False)
                    break
            else:
                union(a,b)
                res.append(True)
        return res