class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def sol(m,s):
            prev = str(startAt)
            res = 0
            if m > 0:
                for ch in str(m):
                    if ch != prev:
                        res += moveCost
                    res += pushCost
                    prev = ch
            s = str(s)
            if len(s) < 2 and m > 0:
                s = '0' + s
            for ch in s:
                if ch != prev:
                    res += moveCost
                res += pushCost
                prev = ch
            # print('--',m,s,res)
            return res
        
        m,s = targetSeconds//60, targetSeconds%60
        res = inf
        if m < 100:
            res = sol(m,s)
        if m > 0 and s+60 < 100:
            res = min(res, sol(m-1, s+60))
        return res