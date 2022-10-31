class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        a = matrix[0]
        for b in matrix[1:]:
            a.pop()
            if a != b[1:]:
                return False
            a.insert(0, b[0])
        return True