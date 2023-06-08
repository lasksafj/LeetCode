class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        tiles = sorted(tiles)
        vis = set()
        res = [0]
        def sol():
            i = 0
            res[0] += 1
            while i < n:
                while i < n and i in vis:
                    i += 1
                if i < n:
                    vis.add(i)
                    sol()
                    vis.remove(i)
                while i < n-1 and tiles[i] == tiles[i+1]:
                    i += 1
                i += 1
        sol()
        return res[0]-1