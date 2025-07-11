class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = [0]*n
        free = list(range(n))
        heapify(free)
        used = []
        for a,b in meetings:
            while used and used[0][0] <= a:
                _,room = heappop(used)
                heappush(free, room)
            if free:
                room = heappop(free)
                heappush(used, [b,room])
                res[room] += 1
            else:
                t,room = heappop(used)
                heappush(used, [b+t-a, room])
                res[room] += 1
        return max(enumerate(res), key=lambda x:x[1])[0]