class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        res = 0
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i, p):
            nonlocal res
            a = values[i]
            for ne in adj[i]:
                if ne != p:
                    a += dfs(ne, i)
            if a % k == 0:
                res += 1
                return 0
            return a
        dfs(0, -1)
        return res