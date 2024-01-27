def kmp_func(s):
    n = len(s)
    pi = [0] * (n)
    for i in range(1,n):
        j = pi[i-1]
        while (j > 0 and s[i] != s[j]):
            j = pi[j-1]
        if (s[i] == s[j]):
            j += 1
        pi[i] = j
    return pi

def f(s,evil):
    kmp = kmp_func(evil)
    @cache
    def dfs(i,j,tight):
        if j == len(evil):
            return 0
        if i == len(s):
            return 1
        res = 0
        for ch in string.ascii_lowercase:
            if tight and ch > s[i]:
                break 
            nj = j
            while nj > 0 and evil[nj] != ch:
                nj = kmp[nj-1]
                
            res = (res + dfs(i+1, nj+1 if (evil[nj]==ch) else 0, tight&(s[i]==ch)))
        return res
    return dfs(0,0,1)

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        return (f(s2,evil) - f(s1,evil) + (evil not in s1)) % 1000000007