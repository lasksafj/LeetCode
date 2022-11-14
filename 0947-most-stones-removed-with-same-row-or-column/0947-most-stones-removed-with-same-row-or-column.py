class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)
        vis = [0] * n
        def dfs(i):
            if vis[i]:
                return 0
            vis[i] = 1
            res = 1
            for ne in adj[i]:
                res += dfs(ne)
            return res
        
        res = 0
        for i in range(n):
            a = 0
            if adj[i] != [] and vis[i] == 0:
                a = -1
                a += dfs(i)
            res += a
        return res
                    