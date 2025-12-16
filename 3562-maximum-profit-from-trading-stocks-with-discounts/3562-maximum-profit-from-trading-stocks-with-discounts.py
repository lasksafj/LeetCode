def merge(A, B):
    N = len(A)
    res = [-inf]*N
    for i in range(N):
        for j in range(N-i):
            res[i+j] = max(res[i+j], A[i] + B[j])
    return res

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = defaultdict(list)
        for a,b in hierarchy:
            adj[a-1].append(b-1)
        def dfs(i):
            dp0 = [0]*(budget+1)
            dp1 = [0]*(budget+1)
            for ne in adj[i]:
                ans0, ans1 = dfs(ne)
                dp0 = merge(dp0, ans0)
                dp1 = merge(dp1, ans1)
            res0 = dp0[:]
            res1 = dp0[:]
            cost = present[i]
            for b in range(cost, budget+1):
                res0[b] = max(res0[b], dp1[b-cost] + future[i]-cost)
            cost //= 2
            for b in range(cost, budget+1):
                res1[b] = max(res1[b], dp1[b-cost] + future[i]-cost)
            return res0, res1
        return dfs(0)[0][-1]