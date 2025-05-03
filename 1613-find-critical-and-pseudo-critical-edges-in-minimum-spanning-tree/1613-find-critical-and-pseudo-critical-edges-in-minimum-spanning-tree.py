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

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def find_bridge(edges):
            nodes = set()
            adj = defaultdict(list)
            idx = defaultdict(int)
            cnt = defaultdict(int)
            all_edge = set()
            for a,b,i in edges:
                adj[a].append(b)
                adj[b].append(a)
                idx[a,b] = i
                idx[b,a] = i
                cnt[a,b] += 1
                cnt[b,a] += 1
                nodes.add(a)
                nodes.add(b)
                all_edge.add(i)
            
            time = [-1] * n
            low = [0] * n
            bridges = set()

            timer = 0
            def dfs(cur, prev):
                nonlocal timer
                time[cur] = low[cur] = timer
                timer += 1
                for ne in adj[cur]:
                    if ne == prev:
                        continue
                    if time[ne] == -1:
                        dfs(ne, cur)
                        # Check if cur-ne is a bridge
                        if time[cur] < low[ne] and cnt[cur,ne] == 1:
                            bridges.add(idx[cur,ne])
                        low[cur] = min(low[cur], low[ne])
                    else:
                        low[cur] = min(low[cur], time[ne])
            for u in nodes:
                if time[u] == -1:
                    dfs(u, -1)
            return bridges, all_edge - bridges
        
        uf = UnionFind(n)
        res = [set(), set()]

        edges = sorted(enumerate(edges), key=lambda y: y[-1][-1])
        for _,E in groupby(edges, key=lambda x: x[-1][-1]):
            tmp_edges = []
            for i, (a,b,w) in E:
                a = uf.root(a)
                b = uf.root(b)
                if a != b:
                    tmp_edges.append([a,b,i])
            bridges, non_bridges = find_bridge(tmp_edges)
            res[0] |= bridges
            res[1] |= non_bridges
            for a,b,i in tmp_edges:
                uf.union(a,b)
        return [list(res[0]), list(res[1])]