class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        l, r = 0, 0
        n = len(tiles)
        window = 0
        ans = 0
        while l < n and r < n:
            if tiles[l][0] + carpetLen > tiles[r][1]:
                window += tiles[r][1] - tiles[r][0] + 1
                ans = max(ans, window)
                r += 1
            else:
                a = window + tiles[l][0] + carpetLen - tiles[r][0]
                ans = max(ans,a)
                window -= tiles[l][1] - tiles[l][0] + 1
                l += 1
        return ans