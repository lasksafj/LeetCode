class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        f = list(range(n+1))
        r = [0]*(n+1)
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
        
        vis = [0] * (n+1)
        for i in range(1, n+1):
            for j in range(1, int(sqrt(i))+1):
                if i%j == 0:
                    if j > threshold:
                        union(i,j)
                    if i//j > threshold:
                        union(i, i//j)

        res = []
        for a,b in queries:
            if root(a) == root(b):
                res.append(True)
            else:
                res.append(False)
        return res