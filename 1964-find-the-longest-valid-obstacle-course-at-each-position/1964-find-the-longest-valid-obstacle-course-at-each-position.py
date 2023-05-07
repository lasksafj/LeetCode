class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        a = [obstacles[0]]
        res = [1]
        for n in obstacles[1:]:
            if n >= a[-1]:
                a.append(n)
                res.append(len(a))
            else:
                p = bisect_right(a, n)
                a[p] = n
                res.append(p+1)
        return res