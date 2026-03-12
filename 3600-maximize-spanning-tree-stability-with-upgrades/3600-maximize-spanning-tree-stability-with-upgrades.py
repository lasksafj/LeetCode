class UF:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n))
        self.r = [0]*n
        self.sz = [1]*n

    def root(self, x):
        if x == self.f[x]:
            return x
        return self.root(self.f[x])
    
    def union(self, a,b):
        a,b = self.root(a), self.root(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            self.f[a] = b
            self.sz[b] += self.sz[a]
        elif self.r[a] > self.r[b]:
            self.f[b] = a
            self.sz[a] += self.sz[b]
        else:
            self.f[a] = b
            self.sz[b] += self.sz[a]
            self.r[b] += 1
        return True

    def size(self, x):
        return self.sz[self.root(x)]

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        uf = UF(n)
        res = inf
        for a,b,s,must in edges:
            if must:
                if not uf.union(a,b): return -1
                res = min(res, s)
        if uf.size(0) == n:
            return res
        edges = [e for e in edges if e[3] == 0]
        edges.sort(key=lambda a:-a[2])
        A = []
        for a,b,s,_ in edges:
            if uf.union(a,b):
                A.append(s)
        if uf.size(0) < n: return -1
        A.sort()
        for i in range(min(k, len(A))):
            A[i] *= 2
        return min(res, min(A))