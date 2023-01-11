class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(cur, prev):
            res = 0
            for ne in adj[cur]:
                if ne != prev:
                    a = dfs(ne, cur)
                    if a > 0 or hasApple[ne]:
                        res += a+2
            return res
        return dfs(0, -1)