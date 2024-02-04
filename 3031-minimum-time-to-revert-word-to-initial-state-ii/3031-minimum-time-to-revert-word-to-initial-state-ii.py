def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        Z = z_function(word)
        res = 1
        for i in range(k, len(word), k):
            if Z[i] == len(word) - i:
                return res
            res += 1
        return res