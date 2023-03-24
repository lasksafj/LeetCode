class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        m = {}
        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
            m[(a,b)] = 1
        res = [0]
        def dfs(cur,prev):
            for ne in adj[cur]:
                if ne != prev:
                    if (cur,ne) in m:
                        res[0] += 1
                    dfs(ne,cur)
        dfs(0,-1)
        return res[0]