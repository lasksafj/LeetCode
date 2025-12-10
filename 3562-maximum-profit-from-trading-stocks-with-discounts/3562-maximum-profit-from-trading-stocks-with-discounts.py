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
                D, no_D = dfs(ne)
                dp1 = merge(dp1, D)
                dp0 = merge(dp0, no_D)
            # current not buy, so children not have discount, default res = dp0
            res0 = dp0[:]
            res1 = dp0[:]
            cost = present[i]
            for b in range(cost, len(dp1)):
                res0[b] = max(dp1[b-cost] + future[i]-cost, res0[b])
            cost //= 2
            for b in range(cost, len(dp1)):
                res1[b] = max(dp1[b-cost] + future[i]-cost, res1[b])
            return res1, res0
        return dfs(0)[1][-1]