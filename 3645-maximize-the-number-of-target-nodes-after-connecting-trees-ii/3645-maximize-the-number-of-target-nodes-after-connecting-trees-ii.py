class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def f(edges):
            adj = defaultdict(list)
            for a,b in edges:
                adj[a].append(b)
                adj[b].append(a)
            N = len(adj)
            color = [0]*N
            def dfs(i,p, d):
                color[i] = d
                for ne in adj[i]:
                    if ne == p: continue
                    dfs(ne, i, d^1)
            dfs(0,-1,0)
            return color
        color1 = f(edges1)
        color2 = f(edges2)
        cnt1 = Counter(color1)
        cnt2 = Counter(color2)
        ma = max(cnt2.values())
        res = [0]*len(color1)
        for i in range(len(color1)):
            res[i] = cnt1[color1[i]] + ma
        return res