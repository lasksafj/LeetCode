class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        s = [ord(ch)-ord('a') for ch in s]
        Ax = [[inf]*2 for _ in range(26)]
        for (x,y),t in zip(points, s):
            x = max(abs(x),abs(y))
            if x < Ax[t][0]:
                Ax[t][1] = Ax[t][0]
                Ax[t][0] = x
            elif x < Ax[t][1]:
                Ax[t][1] = x

        
        radius = min(Ax[i][1] for i in range(26)) - 1
        res = 0
        for x,y in points:
            if abs(x) <= radius and abs(y) <= radius:
                res += 1
        return res
        