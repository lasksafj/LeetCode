class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        n += 1
        top = [0]*n
        bot = [n+1]*n
        left = [n+1]*n
        right = [0]*n
        for x,y in buildings:
            top[y] = max(top[y], x)
            bot[y] = min(bot[y], x)
            left[x] = min(left[x], y)
            right[x] = max(right[x], y)
        res = 0
        for x,y in buildings:
            res += left[x] < y < right[x] and bot[y] < x < top[y]
        return res