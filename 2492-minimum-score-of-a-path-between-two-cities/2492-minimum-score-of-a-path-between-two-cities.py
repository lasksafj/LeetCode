class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        f = list(range(n+1))
        r = [0]*(n+1)
        s = [inf]*(n+1)
        def root(x):
            if x == f[x]:
                return x
            return root(f[x])
        def union(a,b):
            a,b = root(a),root(b)
            if a == b:
                return
            if r[a] < r[b]:
                a,b = b,a
            f[b] = a
            if r[a] == r[b]:
                r[a] += 1
        for a,b,d in roads:
            union(a,b)
        if root(1) != root(n): return -1
        res = inf
        for a,b,d in roads:
            if root(a) == root(1):
                res = min(res, d)
            
        return res