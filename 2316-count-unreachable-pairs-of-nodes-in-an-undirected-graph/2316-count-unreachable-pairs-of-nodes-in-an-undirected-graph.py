class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        r = [0]*n
        def root(x):
            if x == p[x]:
                return x
            return root(p[x])
        def union(a,b):
            a,b = root(a),root(b)
            if r[a] < r[b]:
                p[a] = b
            elif r[a] > r[b]:
                p[b] = a
            else:
                p[a] = b
                r[b] += 1
        for a,b in edges:
            union(a,b)
        p = [root(i) for i in range(n)]
        m = Counter(p)
        if len(m) == 1:
            return 0
        res = 0
        s = 0
        for k in m:
            res += s*m[k]
            s += m[k]
        return res