class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dfs(start, aturn):
            if start == len(stoneValue):
                return 0
            if aturn:
                res = -inf
                s = 0
                for i in range(start, min(len(stoneValue),start+3)):
                    s += stoneValue[i]
                    res = max(res, s + dfs(i+1, aturn^1))
                return res
            else:
                res = inf
                for i in range(start, min(len(stoneValue),start+3)):
                    res = min(res, dfs(i+1, aturn^1))
                return res
        
        a = dfs(0,1)
        b = sum(stoneValue) - a
        if a > b:
            return 'Alice'
        elif a < b:
            return 'Bob'
        return 'Tie'