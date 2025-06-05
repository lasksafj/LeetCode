class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a,b = abs(z-x),abs(z-y)
        if a < b: return 1
        if a > b: return 2
        return 0