class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = s
        no1 = 0
        j = 0
        l = inf
        for i,c in enumerate(s):
            no1 += c == '1'
            while no1 - (s[j] == '1') >= k:
                no1 -= s[j] == '1'
                j += 1
            if no1 == k:
                if i-j < l:
                    res = s[j:i+1]
                    l = i-j
                elif i-j == l:
                    res = min(res, s[j:i+1])
        return res if l < inf else ''