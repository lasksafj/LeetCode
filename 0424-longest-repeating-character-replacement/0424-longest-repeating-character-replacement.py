class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = defaultdict(int)
        n = len(s)
        res = 0
        j = 0
        maxf = 0
        for i in range(n):
            m[s[i]] += 1
            maxf = max(maxf, m[s[i]])
            if i-j+1-maxf > k:
                m[s[j]] -= 1
                j += 1
            res = max(res, i-j+1)
        return res