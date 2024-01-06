def f(num,limit,s):
    if len(num) < len(s):
        return 0
    @cache
    def dfs(i,prev):
        if i == len(num):
            return 1
        if i + len(s) >= len(num):
            d = int(s[len(s) - (len(num) - i)])
            if not prev or d <= int(num[i]):
                return dfs(i+1,prev&(d == int(num[i])))
            return 0
            
        if prev:
            k = min(limit, int(num[i])) + 1
        else:
            k = limit + 1
        res = 0
        for d in range(k):
            res += dfs(i+1, prev&(d == int(num[i])))
        return res
    return dfs(0,1)

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        a = f(str(finish),limit,s)
        b = f(str(start-1),limit,s)
        return a-b