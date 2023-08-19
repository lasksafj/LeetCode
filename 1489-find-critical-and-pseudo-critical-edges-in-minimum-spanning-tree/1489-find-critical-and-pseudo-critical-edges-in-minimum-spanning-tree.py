class Solution:
    class UnionFind:
        def __init__(self, n):
            self.f = list(range(n))
            self.r = [0]*n
            self.size = [1]*n
            self.max_size = 1
        def root(self, x):
            if x == self.f[x]:
                return x
            return self.root(self.f[x])
        def union(self,a,b):
            a,b = self.root(a),self.root(b)
            if a == b:
                return False
            if self.r[a] < self.r[b]:
                self.f[a] = b
                self.size[b] += self.size[a]
            elif self.r[a] > self.r[b]:
                self.f[b] = a
                self.size[a] += self.size[b]
            else:
                self.f[a] = b
                self.size[b] += self.size[a]
                self.r[b] += 1
            self.max_size = max(self.max_size, self.size[a], self.size[b])
            return True
    
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = [edge.copy() for edge in edges]
        for i, edge in enumerate(new_edges):
            edge.append(i)
        new_edges.sort(key=lambda x: x[2])
        
        uf_std = self.UnionFind(n)
        std_weight = 0
        for u, v, w, _ in new_edges:
            if uf_std.union(u, v):
                std_weight += w
        
        critical = []
        pseudo_critical = []
        for (u, v, w, i) in new_edges:
            uf_ignore = self.UnionFind(n)
            ignore_weight = 0
            for (x, y, w_ignore, j) in new_edges:
                if i != j and uf_ignore.union(x, y):
                    ignore_weight += w_ignore
            if uf_ignore.max_size < n or ignore_weight > std_weight:
                critical.append(i)
                continue
            uf_force = self.UnionFind(n)
            force_weight = w
            uf_force.union(u, v)
            for (x, y, w_force, j) in new_edges:
                if i != j and uf_force.union(x, y):
                    force_weight += w_force
            if force_weight == std_weight:
                pseudo_critical.append(i)
        return [critical, pseudo_critical]