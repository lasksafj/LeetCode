class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(i, op):
            if i == n:
                return ['']
            res = []
            if op:
                for s in dfs(i+1, op-1):
                    res.append(')' + s)
            if op < n-i:
                for s in dfs(i, op+1):
                    res.append('(' + s)
            return res
        return dfs(0, 0)