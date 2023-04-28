class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                connect = True
                a = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        if a == 0:
                            l = strs[i][k]
                            r = strs[j][k]
                        elif a == 1:
                            if r != strs[i][k] or l != strs[j][k]:
                                connect = False
                                break
                        elif a == 2:
                            connect = False
                            break
                        a += 1
                if (connect and a == 2) or a == 0:
                    adj[i].append(j)
                    adj[j].append(i)
        vis = [0]*n
        # print(adj)
        res = 0
        def dfs(i):
            vis[i] = True
            for ne in adj[i]:
                if not vis[ne]:
                    dfs(ne)
        for i in range(n):
            if not vis[i]:
                dfs(i)
                res += 1
        return res