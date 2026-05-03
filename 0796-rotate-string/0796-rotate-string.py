def Z_func(s):
    N = len(s)
    res = [0]*N
    l,r = 0,0
    for i in range(1,N):
        if i < r:
            res[i] = min(res[i-l], r-i)
        while i+res[i] < N and s[res[i]] == s[i+res[i]]:
            res[i] += 1
        if i+res[i] > r:
            l = i
            r = i+res[i]
    return res

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        a = goal + '#' + s + s
        Z = Z_func(a)
        for i in range(len(goal)+1, len(Z) - len(s)):
            if Z[i] == len(goal):
                return True
        return False