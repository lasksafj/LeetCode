def isSubsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        W = sorted([c for c,v in Counter(s).items() if v >= k])
        q = deque([''])
        res = ''
        while q:
            for _ in range(len(q)):
                res = q.popleft()
                for c in W:
                    tmp = res + c
                    if isSubsequence(tmp*k, s):
                        q.append(tmp)
        return res