class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i,cnt):
            if cnt < 0:
                return False
            if i == len(s):
                return cnt == 0
            if s[i] == '(':
                return dfs(i+1,cnt+1)
            elif s[i] == ')':
                return dfs(i+1,cnt-1)
            return dfs(i+1,cnt) or dfs(i+1,cnt+1) or dfs(i+1,cnt-1)
        return dfs(0,0)