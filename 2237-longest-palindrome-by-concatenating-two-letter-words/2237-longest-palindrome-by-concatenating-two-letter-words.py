class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        res = 0
        center = 0
        for w in cnt:
            wr = w[::-1]
            if w == wr:
                res += cnt[w]//2 * 2
                if cnt[w] & 1:
                    center = 1
            elif wr in cnt:
                res += min(cnt[w], cnt[wr])
        return (res + center)*2