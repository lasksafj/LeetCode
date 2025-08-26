class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = max(dimensions, key=lambda x: (x[0]**2 + x[1]**2, x[0]*x[1]))
        return res[0]*res[1]