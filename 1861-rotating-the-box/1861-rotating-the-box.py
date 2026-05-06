class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M,N = len(box),len(box[0])
        res = [['.']*M for _ in range(N)]
        for i in range(M):
            bot = N-1
            for j in range(N-1,-1,-1):
                if box[i][j] == '#':
                    res[bot][M-i-1] = '#'
                    bot -= 1
                elif box[i][j] == '*':
                    res[j][M-i-1] = '*'
                    bot = j-1
        return res