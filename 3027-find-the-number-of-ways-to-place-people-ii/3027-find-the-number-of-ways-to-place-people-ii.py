
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0], -x[1]))
        N = len(points)
        res = 0
        for i in range(N):
            a,b = points[i]
            largest_d = -inf
            for j in range(i+1,N):
                c,d = points[j]
                if d <= b:
                    if d > largest_d:
                        res += 1
                        largest_d = d
        return res