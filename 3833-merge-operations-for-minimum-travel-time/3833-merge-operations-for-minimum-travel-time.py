class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        preT = list(accumulate(time))
        @cache
        def dfs(a,b, k):
            if b == n-1:
                return 0 if k == 0 else inf
            t = preT[b] - (preT[a] if a >= 0 else 0)
            res = inf
            for c in range(b+1, n):
                if k >= c-b-1:
                    res = min(res, dfs(b, c, k-(c-b-1)) + (position[c] - position[b]) * t)
            return res
        return dfs(-1,0,k)   