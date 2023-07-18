class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in roads:
            adj[a].append(b)
            adj[b].append(a)
        A = [0]*n
        k = n
        for _,i in sorted([(len(adj[i]),i) for i in adj], reverse=True):
            A[i] = k
            k -= 1
        vis = set()
        # print(A)
        def dfs(i):
            res = 0
            if i in vis:
                return 0
            vis.add(i)
            for ne in adj[i]:
                res += dfs(ne) + A[i] + A[ne]
            return res
        res = 0
        for i in range(n):
            if i not in vis:
                res += dfs(i)
        return res//2