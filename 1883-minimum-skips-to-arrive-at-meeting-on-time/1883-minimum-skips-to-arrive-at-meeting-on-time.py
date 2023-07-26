class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        N = len(dist)
        eps=1e-9
        @cache
        def dfs(i, k):
            if k < 0:
                return inf
            if i == N:
                return 0
            h = dist[i]/speed
            return min(ceil(dfs(i+1, k) + h - eps), dfs(i+1, k-1) + h)
        print(dfs(0,7))
        for k in range(N+1):
            if dfs(0,k) <= hoursBefore:
                return k
        return -1