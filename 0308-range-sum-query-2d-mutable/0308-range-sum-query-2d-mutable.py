def lowbit(n):
    return n&(-n)
class BIT2D:
    def __init__(self, matrix: List[List[int]]):
        self.M = M = len(matrix)+1
        self.N = N = len(matrix[0])+1
        self.BIT = [[0]*N for _ in range(M)]
        for i in range(M-1):
            for j in range(N-1):
                self.update(i,j, matrix[i][j])
    def update(self, row: int, col: int, diff: int) -> None:
        i = row+1
        while i < self.M:
            j = col+1
            while j < self.N:
                self.BIT[i][j] += diff
                j += lowbit(j)
            i += lowbit(i)
    def query(self, row, col):
        res = 0
        i = row+1
        while i:
            j = col+1
            while j:
                res += self.BIT[i][j]
                j -= lowbit(j)
            i -= lowbit(i)
        return res

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.T = BIT2D(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        old_val = self.sumRegion(row, col, row, col)
        self.T.update(row, col, val - old_val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.T.query(row2, col2) 
                - self.T.query(row1-1, col2) 
                - self.T.query(row2, col1-1) 
                + self.T.query(row1-1, col1-1))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)