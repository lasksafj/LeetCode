class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = [0] * n
        def dfs(prev, cur):
            m = defaultdict(int)
            m[labels[cur]] = 1
            for ne in adj[cur]:
                if ne != prev:
                    for c,v in dfs(cur, ne).items():
                        m[c] += v
            res[cur] = m[labels[cur]]
            return m
        dfs(-1, 0)
        return res
                    