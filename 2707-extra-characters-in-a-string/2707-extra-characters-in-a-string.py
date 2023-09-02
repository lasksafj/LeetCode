class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        
        @cache
        def dfs(i):
            if i >= len(s):
                return 0
            res = inf
            for j in range(i+1, 52):
                if s[i:j] in dictionary:
                    res = min(res, dfs(j))
                else:
                    res = min(res, dfs(j) + j-i)
            return res
        
        return dfs(0)