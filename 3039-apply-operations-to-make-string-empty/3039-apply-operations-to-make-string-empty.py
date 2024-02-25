class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        ma = max(cnt.values())
        res = []
        for ch in s[::-1]:
            if cnt[ch] == ma:
                res.append(ch)
                cnt[ch] -= 1
        return ''.join(res)[::-1]