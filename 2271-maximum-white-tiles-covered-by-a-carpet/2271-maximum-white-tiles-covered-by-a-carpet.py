class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        res = 0
        A = [0]*len(tiles)
        A[0] = tiles[0][1]-tiles[0][0]+1
        for i in range(1, len(tiles)):
            a,b = tiles[i]
            A[i] = A[i-1] + b-a+1
        # print(A)
        for i in range(len(tiles)):
            
            a,b = tiles[i]
            if b-a+1 >= carpetLen:
                return carpetLen
            x = max(0,b-carpetLen)
            p = max(0, bisect_right(tiles, [x,inf]) - 1)
            res = max(res, A[i] - A[p] + max(0, tiles[p][1] - max(x, tiles[0][0]-1)))
            
            # print(i)
            # print('---- x',x)
            # print('---- p',p)
            # print('---- res',res)
        return res