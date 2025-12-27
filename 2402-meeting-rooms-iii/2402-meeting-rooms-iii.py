class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = list(range(n))
        heapify(free)
        used = []
        res = [0]*n
        cur = 0
        for a,b in meetings:
            cur = max(cur, a)
            if not free:
                cur = max(cur, used[0][0])
            while used and used[0][0] <= cur:
                heappush(free, heappop(used)[1])
            r = heappop(free)
            res[r] += 1
            heappush(used, [cur+b-a, r])
        return max(list(range(n)), key=lambda r: [res[r], -r])