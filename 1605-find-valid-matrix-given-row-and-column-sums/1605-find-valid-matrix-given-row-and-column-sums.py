class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        i,j = 0,0
        cur = rowSum[i]
        res = [[0]*len(colSum) for _ in range(len(rowSum))]
        while i < len(rowSum) and j < len(colSum):
            cur = min(rowSum[i], colSum[j])
            res[i][j] = cur
            rowSum[i] -= cur 
            colSum[j] -= cur
            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        return res