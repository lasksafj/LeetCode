class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in pairs:
            g[u].add(v)
            g[v].add(u)
        n = len(g)
        for i in g:
            g[i].add(i)
        
        def dfs(root, nodes):
            res = 1
            for p in g[root]:
                if p == root:
                    continue
                if p not in nodes:
                    return 0
                if g[p] == g[root]:
                    res = 2
                g[p].remove(root)
            to_try = sorted([[len(g[p]), p] for p in g[root] if p != root], reverse=True)
            for l,p in to_try:
                if l >= 2 and l == len(g[p]):
                    w = dfs(p, nodes & g[p])
                    if w == 0:
                        return 0
                    if w == 2:
                        res = 2
            return res
        for i in g:
            if len(g[i]) == n:
                return dfs(i, g[i])
        return 0