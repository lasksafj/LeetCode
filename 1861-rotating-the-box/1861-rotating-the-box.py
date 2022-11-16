class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n = len(box), len(box[0])
        res = [['.'] * m for _ in range(n)]
        for i in range(m):
            bottom = n
            for j in range(n-1, -1, -1):
                if box[i][j] == '#':
                    bottom -= 1
                    res[bottom][m-i-1] = '#'
                elif box[i][j] == '*':
                    bottom = j
                    res[bottom][m-i-1] = '*'
        return res