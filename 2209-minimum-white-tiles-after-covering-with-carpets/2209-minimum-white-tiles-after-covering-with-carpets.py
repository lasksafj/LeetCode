class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        suf = [0]*len(floor)
        s = 0
        for i in range(len(floor)-1,-1,-1):
            if floor[i] == '1':
                s += 1
            suf[i] = s
        @cache
        def dfs(i,k):
            if i >= len(floor):
                return 0
            if k == 0:
                return suf[i]
            if floor[i] == '0':
                return dfs(i+1,k)
            return min(dfs(i+1,k) + 1, dfs(i+carpetLen,k-1))
        return dfs(0,numCarpets)