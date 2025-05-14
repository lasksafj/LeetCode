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
            return
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

    def size(self, x):
        return self.sz[self.root(x)]

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(A,B):
            res = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    res += 1
                    if res == 3:
                        return False
            return True

        N = len(strs)
        uf = UF(N)
        for i in range(N):
            for j in range(i+1, N):
                if is_similar(strs[i], strs[j]):
                    uf.union(i,j)
        
        return len(set(uf.root(i) for i in range(N)))