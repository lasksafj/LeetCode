class Spreadsheet:

    def __init__(self, rows: int):
        self.C = [defaultdict(int) for _ in range(rows+1)]

    def setCell(self, cell: str, value: int) -> None:
        col,row = cell[0], int(cell[1:])
        self.C[row][col] = value
    
    def getCell(self, cell):
        try:
            return int(cell)
        except:
            col,row = cell[0], int(cell[1:])
            return self.C[row][col]

    def resetCell(self, cell: str) -> None:
        col,row = cell[0], int(cell[1:])
        self.C[row][col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:].split('+')
        return self.getCell(formula[0]) + self.getCell(formula[1])


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)