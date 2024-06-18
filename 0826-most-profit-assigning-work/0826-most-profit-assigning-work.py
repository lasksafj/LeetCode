class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        P = sorted(list(range(len(difficulty))), key=lambda i:difficulty[i])
        res = 0
        i = 0
        ma = 0
        for w in worker:
            while i < len(difficulty) and difficulty[P[i]] <= w:
                ma = max(ma, profit[P[i]])
                i += 1
            if ma:
                res += ma
        return res