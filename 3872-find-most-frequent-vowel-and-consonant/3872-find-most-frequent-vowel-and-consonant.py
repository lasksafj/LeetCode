class Solution:
    def maxFreqSum(self, s: str) -> int:
        return max([b for a,b in Counter(s).items() if a in 'aeiou'], default=0) + max([b for a,b in Counter(s).items() if a not in 'aeiou'], default=0)