class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dfs(i, prev):
            if i == len(stones)-1:
                return True
            k = stones[i] - stones[prev]
            ne = stones[i] + k
            p = bisect_left(stones, ne)
            if i < p < len(stones) and abs(stones[p] - stones[i] - k) <= 1 and dfs(p, i):
                return True
            if i < p-1 < len(stones) and abs(stones[p-1] - stones[i] - k) <= 1 and dfs(p-1, i):
                return True
            if i < p+1 < len(stones) and abs(stones[p+1] - stones[i] - k) <= 1 and dfs(p+1, i):
                return True
            return False
        if stones[1] - stones[0] != 1:
            return False
        return dfs(1, 0)