class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()
        res = 0
        i = 0
        pq = []
        cur = 1
        while i < N or pq:
            while i < N  and events[i][0] == cur:
                heappush(pq, events[i][1])
                i += 1
            while pq and pq[0] < cur:
                heappop(pq)
            if pq:
                heappop(pq)
                res += 1
            cur += 1
        return res
            