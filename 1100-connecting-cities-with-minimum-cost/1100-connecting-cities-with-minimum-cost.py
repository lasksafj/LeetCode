class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        n += 1
        p = list(range(n))
        R = [0]*n
        def root(u):
            while u != p[u]:
                u = p[u]
            return u
        def union(u,v):
            u,v = root(u),root(v)
            if u==v: return False
            if R[u] < R[v]:
                u,v = v,u
            p[v] = u
            if R[u]==R[v]:
                R[u] += 1
            return True
        res = 0
        for a,b,c in sorted(connections, key=lambda e:e[2]):
            res += c if union(a,b) else 0
        return res if len(set(root(i) for i in range(1,n))) == 1 else -1