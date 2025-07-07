class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        res = 0
        t = 0
        i = 0
        N = len(events)
        pq = []
        while i < N or pq:
            if i < N and t < events[i][0]:
                t = events[i][0]
            while i < N and events[i][0] <= t:
                heappush(pq, events[i][1])
                i += 1
            while pq:
                d = heappop(pq)
                if d >= t:
                    t += 1
                    res += 1
                if i < N and t == events[i][0]:
                    break
        return res
