class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        edge = s // 4
        if edge * 4 != s:
            return False
        @cache
        def dfs(k, cur, mask):
            if k == 4:
                return True
            if cur == edge:
                return dfs(k+1,0,mask)
            for j in range(len(matchsticks)):
                if (1<<j)&mask == 0 and cur+matchsticks[j] <= edge and dfs(k, cur+matchsticks[j], (1<<j)|mask):
                    return True
            return False
        return dfs(0,0,0)