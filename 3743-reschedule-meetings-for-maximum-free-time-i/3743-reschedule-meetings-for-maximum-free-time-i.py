class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)
        t = 0
        for i in range(k):
            t += endTime[i] - startTime[i]
        l,r = 0,0
        res = 0
        for i in range(N-k+1):
            a,b = startTime[i], endTime[i]
            c,d = eventTime,eventTime
            if i+k < N:
                c,d = startTime[i+k], endTime[i+k]
            r = c
            res = max(res, r-l-t)
            t = t - (b-a) + (d-c)
            l = b
        return res