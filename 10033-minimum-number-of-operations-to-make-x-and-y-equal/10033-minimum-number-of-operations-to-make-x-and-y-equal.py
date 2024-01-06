class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def dfs(x):
            # print(x)
            if x <= y:
                return y-x
            a = dfs((x+10)//11) + (11-x%11)%11
            b = dfs((x+4)//5) + (5-x%5)%5
            c = dfs(x-1)
            return min(a,b,c)+1
        return dfs(x)