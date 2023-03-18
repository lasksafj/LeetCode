class Solution:
    def racecar(self, target: int) -> int:
        pq = [[0, 0, 1]]
        m = defaultdict(int)
        while pq:
            step,cur,speed = heapq.heappop(pq)
            if cur == target:
                return step
            heapq.heappush(pq, [step+1, cur+speed, speed*2])
            if (cur+speed > target and speed > 0) or (cur+speed < target and speed < 0):
                heapq.heappush(pq, [step+1, cur, -speed//abs(speed)])

        return 1