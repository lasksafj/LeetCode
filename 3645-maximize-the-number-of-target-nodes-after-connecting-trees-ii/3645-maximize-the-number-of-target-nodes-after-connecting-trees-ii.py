class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def f(edges):
            adj = defaultdict(list)
            for a,b in edges:
                adj[a].append(b)
                adj[b].append(a)
            N = len(adj)
            dp = [[0]*2 for _ in range(N)]
            def dfs(i,p):
                e,o = 0,0
                for ne in adj[i]:
                    if ne == p: continue
                    ne, no = dfs(ne, i)
                    e += no
                    o += ne
                dp[i] = [e+1, o]
                return dp[i]
            dfs(0, -1)
            ans = [[0]*2 for _ in range(N)]
            def dfs2(i,p, e,o):
                ans[i] = [e,o]
                for ne in adj[i]:
                    if ne == p: continue
                    dfs2(ne, i, o, e)
            dfs2(0, -1, dp[0][0], dp[0][1])
            return ans
        A = f(edges1)
        B = f(edges2)
        ma_odd2 = max([o for _,o in B])
        return [a + ma_odd2 for a,_ in A]