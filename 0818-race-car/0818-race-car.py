class Solution:
    def racecar(self, target: int) -> int:
        q = deque([[0, 0, 1]])
        m = defaultdict(int)
        while q:
            step,cur,speed = q.popleft()
            if cur == target:
                return step
            q.append([step+1, cur+speed, speed*2])
            if (cur+speed > target and speed > 0) or (cur+speed < target and speed < 0):
                q.append([step+1, cur, -speed//abs(speed)])

        return 1