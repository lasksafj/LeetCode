from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0], -x[1]))
        N = len(points)
        res = 0
        for i in range(N):
            a,b = points[i]
            A = SortedList()
            for j in range(i+1,N):
                c,d = points[j]
                if d <= b:
                    res += (A.bisect_right(b) - A.bisect_left(d) == 0)
                A.add(d)
        return res