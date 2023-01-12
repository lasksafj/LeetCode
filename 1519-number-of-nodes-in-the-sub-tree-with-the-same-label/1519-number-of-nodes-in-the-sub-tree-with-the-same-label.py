class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = [0] * n
        m = defaultdict(int)
        def dfs(prev, cur, m):
            bef = m[labels[cur]]
            for ne in adj[cur]:
                if ne != prev:
                    dfs(cur, ne, m)
            m[labels[cur]] += 1
            res[cur] = m[labels[cur]] - bef

        dfs(-1, 0, m)
        return res
                    