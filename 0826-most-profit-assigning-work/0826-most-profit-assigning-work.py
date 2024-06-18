class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        P = sorted(list(range(len(difficulty))), key=lambda i:difficulty[i])
        res = 0
        pq = []
        i = 0
        for w in worker:
            while i < len(difficulty) and difficulty[P[i]] <= w:
                heappush(pq, -profit[P[i]])
                i += 1
            if pq:
                res += -pq[0]
        return res