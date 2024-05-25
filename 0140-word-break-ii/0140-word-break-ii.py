class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        def dfs(i, cur, path):
            if i == len(s):
                if cur in wordDict:
                    res.append(' '.join(path + [cur]))
                return
            dfs(i+1, cur+s[i], path)
            if cur in wordDict:
                dfs(i+1, s[i], path + [cur])
        dfs(0,'',[])
        return res