class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        bit_len = int(log2(n)) + 1
        pos = [[-1]*(bit_len+1) for _ in range(n)]
        m = [[-1]*27 for _ in range(n)]
        H = [0]*n
        adj = defaultdict(list)
        for a,b,w in edges:
            adj[a].append([b,w])
            adj[b].append([a,w])
        
        def dfs(prev, cur, d, h):
            m[cur] = m[prev][:]
            m[cur][d] += 1
            H[cur] = h
            pos[cur][0] = prev
            for i in range(1, bit_len+1):
                if pos[cur][i-1] == -1:
                    break
                pos[cur][i] = pos[pos[cur][i-1]][i-1]
            
            for ne,w in adj[cur]:
                if ne != prev:
                    dfs(cur, ne, w, h+1)
        
        dfs(-1, 0, 0, 0)
        
        def lca(u,v):
            if H[u] < H[v]:
                u,v = v,u
            k = H[u] - H[v]
            for i in range(bit_len, -1, -1):
                if k&(1<<i):
                    u = pos[u][i]
            if u == v:
                return u
            for i in range(bit_len, -1, -1):
                if pos[u][i] != pos[v][i]:
                    u,v = pos[u][i], pos[v][i]
            return pos[u][0]
        
        res = []
        for a,b in queries:
            k = lca(a,b)
            freq = [m[a][i] + m[b][i] - 2*m[k][i] for i in range(27)]
            res.append(sum(freq) - max(freq))
        return res