class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        idx = sorted([i for i in range(n)], key=lambda x: endTime[x])
        startTime = [startTime[i] for i in idx]
        endTime = [endTime[i] for i in idx]
        profit = [profit[i] for i in idx]
        # print(startTime, endTime, profit)
        prof = {}
        prof[0] = 0
        prof[endTime[0]] = profit[0]
        res = 0
        for i in range(1, n):
            start = bisect.bisect(endTime, startTime[i]) - 1
            if start == -1:
                start = 0
            else:
                start = endTime[start]
            prof[endTime[i]] = max(prof[endTime[i-1]], prof[start] + profit[i])
            res = prof[endTime[i]]
        # print(prof)
        return res
            