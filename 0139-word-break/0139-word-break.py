class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def dfs(i):
            if i == len(s):
                return True
            for j in range(i+1, i+21):
                if s[i:j] in wordDict:
                    if dfs(j):
                        return True
            return False
        return dfs(0)