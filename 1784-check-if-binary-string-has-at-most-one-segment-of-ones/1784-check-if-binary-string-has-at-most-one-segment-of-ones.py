class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = '0'+s
        return s.count('01') == 1