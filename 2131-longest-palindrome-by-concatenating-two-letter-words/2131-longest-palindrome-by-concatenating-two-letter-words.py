class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        # print(count)
        res,same = 0,0
        for w, cnt in count.items():
            if w[0] == w[1]:
                res += cnt//2 * 2
                if cnt%2:
                    if same == 0:
                        same = 1
            else:
                res += min(cnt, count[w[::-1]])
        return (res+same) * 2