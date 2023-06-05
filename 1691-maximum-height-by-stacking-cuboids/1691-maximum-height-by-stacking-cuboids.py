class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        from itertools import permutations
        cuboids = [sorted(cuboids[i]) for i in range(len(cuboids))]
        cuboids.sort()
        @cache
        def dfs(i, pw, pl, ph):
            if i == len(cuboids):
                return 0
            res = 0
            w,l,h = cuboids[i]
            if pw <= w and pl <= l and ph <= h:
                res = max(res, h + dfs(i+1, w, l, h))
            res = max(res, dfs(i+1, pw, pl, ph))
            return res
        return dfs(0, 0, 0, 0)