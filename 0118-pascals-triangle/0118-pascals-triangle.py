class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            tmp = []
            for j in range(i+1):
                tmp.append((res[i-1][j] if j < i else 0) + (res[i-1][j-1] if j > 0 else 0))
            res.append(tmp)
        return res