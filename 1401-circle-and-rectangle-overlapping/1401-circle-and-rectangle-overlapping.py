class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        d = 0
        if xCenter < x1 or xCenter > x2:
            d += min((x1-xCenter)**2, (xCenter-x2)**2)
        if yCenter < y1 or yCenter > y2:
            d += min((y1-yCenter)**2, (yCenter-y2)**2)
        return d <= radius**2