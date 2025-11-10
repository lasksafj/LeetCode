class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        res = []
        for i in range(sideLength):
            for j in range(sideLength):
                a = (width//sideLength + (j < width%sideLength))* (height//sideLength + (i < height%sideLength))
                res.append(a)
        return sum(sorted(res)[::-1][:maxOnes])