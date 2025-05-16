class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        dp = [[1, N] for _ in range(N)]
        mp = {}
        start = N-1
        for i in range(N-1,-1,-1):
            w = words[i]
            for j in range(len(w)):
                for c in ascii_letters:
                    if c == w[j]:
                        continue
                    tmp = w[:j] + c + w[j+1:]
                    if tmp in mp:
                        k = mp[tmp]
                        if groups[i] == groups[k]:
                            continue
                        if dp[i][0] < dp[k][0] + 1:
                            dp[i] = [dp[k][0] + 1, k]
            if dp[i][0] > dp[start][0]:
                start = i
            mp[w] = i
        i = start
        res = []
        while i < N:
            res.append(words[i])
            i = dp[i][1]
        return res