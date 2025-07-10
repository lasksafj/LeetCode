class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)
        L = [0]*N
        R = [0]*N
        res = 0
        for i in range(N):
            L[i] = max(L[i-1] if i else 0, startTime[i] - (endTime[i-1] if i else 0))
        for i in range(N-1,-1,-1):
            R[i] = max(R[i+1] if i+1<N else 0, (startTime[i+1] if i+1<N else eventTime) - endTime[i])
        for i in range(N):
            ma = 0
            if i:
                ma = max(ma, L[i-1])
            if i+1<N:
                ma = max(ma, R[i+1])
            cur = (startTime[i+1] if i+1<N else eventTime) - (endTime[i-1] if i else 0)
            if ma < endTime[i] - startTime[i]:
                cur -= endTime[i] - startTime[i]
            res = max(res, cur)
        return res