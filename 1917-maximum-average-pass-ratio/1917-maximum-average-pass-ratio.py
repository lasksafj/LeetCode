class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        for a,b in classes:
            heappush(pq, [a/b - (a+1)/(b+1),a,b])
        while extraStudents:
            _,a,b = heappop(pq)
            a += 1
            b += 1
            heappush(pq, [a/b - (a+1)/(b+1),a,b])
            extraStudents -= 1
        return sum(a/b for _,a,b in pq) / len(classes)