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
        for i in range(threshold+1, n+1):
            if vis[i]:
                continue
            vis[i] = 1
            for j in range(i+i, n+1, i):
                union(i,j)
                if not vis[j]:
                    vis[j] = 1

        res = []
        for a,b in queries:
            if root(a) == root(b):
                res.append(True)
            else:
                res.append(False)
        return res