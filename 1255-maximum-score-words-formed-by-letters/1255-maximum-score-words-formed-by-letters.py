class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        mp = defaultdict(int)
        for ch in letters:
            mp[ch] += 1
        def dfs(i,mp):
            if i == len(words):
                return 0
            res = dfs(i+1, mp)
            tmp = mp.copy()
            ok = True
            s = 0
            for ch in words[i]:
                if tmp[ch] > 0:
                    tmp[ch] -= 1
                    s += score[ord(ch)-ord('a')]
                else:
                    ok = False
                    break
            if ok:
                mp = tmp
                res = max(res, dfs(i+1, mp) + s)
            return res
        return dfs(0,mp)