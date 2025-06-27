def issub(s,t):
    s = iter(s)
    return all(c in s for c in t)

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        W = sorted(c for c,v in Counter(s).items() if v >= k)
        q = deque([''])
        res = ''
        while q:
            for _ in range(len(q)):
                res = q.popleft()
                for c in W:
                    tmp = res+c
                    if issub(s, tmp*k):
                        q.append(tmp)
        return res