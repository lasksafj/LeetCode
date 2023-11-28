class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9+7
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            res = 0
            if s[i] == '*':
                res += 9*dfs(i+1)
                if i+1 < len(s):
                    if s[i+1] == '*':
                        res += 15*dfs(i+2)
                    else:
                        res += dfs(i+2)
                        if s[i+1] <= '6':
                            res += dfs(i+2)
            else:
                res += dfs(i+1)
                if s[i] == '1':
                    if i+1 < len(s):
                        if s[i+1] == '*':
                            res += 9*dfs(i+2)
                        else:
                            res += dfs(i+2)
                elif s[i] == '2':
                    if i+1 < len(s):
                        if s[i+1] == '*':
                            res += 6*dfs(i+2)
                        elif s[i+1] <= '6':
                            res += dfs(i+2)
            return res % mod
        return dfs(0)
                    
