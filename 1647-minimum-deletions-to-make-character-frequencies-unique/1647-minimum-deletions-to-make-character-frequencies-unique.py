class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        s = set()
        for cnt in freq.values():
            while cnt in s and cnt > 0:
                cnt -= 1
                res += 1
            if cnt > 0:
                s.add(cnt)
        return res
            
                