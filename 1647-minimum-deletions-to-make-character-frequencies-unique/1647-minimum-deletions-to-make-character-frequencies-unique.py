class Solution:
    def minDeletions(self, s: str) -> int:
        A = Counter(s).values()
        res = 0
        s = set()
        for n in A:
            while n > 0 and n in s:
                n -= 1
                res += 1
            s.add(n)
        return res
        