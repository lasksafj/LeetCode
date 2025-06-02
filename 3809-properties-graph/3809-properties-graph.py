class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        N = len(properties)
        f = list(range(N))
        r = [0]*N
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


        for i in range(N):
            for j in range(i):
                if len(set(properties[i]) & set(properties[j])) >= k:
                    union(i,j)
        return len(set(root(i) for i in range(N)))