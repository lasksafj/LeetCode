class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        f = list(range(n))
        r = [0]*n
        v = [-1]*n
        def root(x):
            if x == f[x]:
                return x
            return root(f[x])
        def union(a,b,w):
            a,b = root(a),root(b)
            if a == b:
                v[a] &= w
                return
            if v[a] == v[b] == -1:
                q = w
            elif v[a] == -1:
                q = w & v[b]
            elif v[b] == -1:
                q = w & v[a]
            else:
                q = w & v[a] & v[b]
            
            if r[a] < r[b]:
                f[a] = b
                v[b] = q
            elif r[a] > r[b]:
                f[b] = a
                v[a] = q
            else:
                f[a] = b
                r[b] += 1
                v[b] = q
        
        for a,b,w in edges:
            union(a,b,w)
        res = []
        for a,b in query:
            if root(a) == root(b):
                res.append(v[root(a)])
            else:
                res.append(-1)
        return res