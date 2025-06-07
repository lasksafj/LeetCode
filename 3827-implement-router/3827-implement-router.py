class Router:

    def __init__(self, memoryLimit: int):
        self.dq = deque()
        self.S = set()
        self.mpA = defaultdict(list)
        self.mpI = defaultdict(int)
        self.k = memoryLimit
        self.cur = 0

    def addPacket(self, s: int, d: int, t: int) -> bool:
        dq,S,mpA = self.dq, self.S, self.mpA
        if (s,d,t) in S:
            return False
        if self.k == 0:
            self.forwardPacket()
        self.k -= 1
        S.add((s,d,t))
        mpA[d].append((t, s))
        dq.append((s,d,t))
        return True

    def forwardPacket(self) -> List[int]:
        dq,S,mpA = self.dq, self.S, self.mpA
        if not dq: return []
        self.k += 1
        s,d,t = dq.popleft()
        S.remove((s,d,t))
        self.mpI[d] += 1
        return [s,d,t]

    def getCount(self, d: int, s: int, e: int) -> int:
        mpA, mpI = self.mpA, self.mpI
        return max(mpI[d], bisect_right(mpA[d], e, key=lambda x:x[0])) - max(mpI[d], bisect_left(mpA[d], s, key=lambda x:x[0]))


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)