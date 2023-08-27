class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mp = {}
        for i,st in enumerate(stones):
            mp[st] = i
        @cache
        def dfs(i, prev):
            if i == len(stones)-1:
                return True
            k = stones[i] - stones[prev]
            for ne in range(stones[i] + k-1, stones[i] + k+2):
                if ne in mp and i < mp[ne] and dfs(mp[ne], i):
                    return True
            return False
        if stones[1] - stones[0] != 1:
            return False
        return dfs(1, 0)