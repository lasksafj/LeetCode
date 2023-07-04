class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        no_unique = len(Counter(s))
        res = 0
        for unique in range(1,no_unique+1):
            good_char = 0
            j = 0
            m = defaultdict(int)
            for i in range(len(s)):
                m[s[i]] += 1
                if m[s[i]] == k:
                    good_char += 1
                while len(m) > unique:
                    m[s[j]] -= 1
                    if m[s[j]] == k-1:
                        good_char -= 1
                    if m[s[j]] == 0:
                        del m[s[j]]
                    j += 1
                if good_char == unique:
                    res = max(res, i-j+1)
        return res