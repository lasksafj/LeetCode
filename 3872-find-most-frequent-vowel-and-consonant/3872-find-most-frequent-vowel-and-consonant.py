class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = Counter(s)
        res1=res2=0
        for a,b in cnt.items():
            if a in 'aeiou':
                res1 = max(res1, b)
            else:
                res2 = max(res2, b)
        return res1+res2