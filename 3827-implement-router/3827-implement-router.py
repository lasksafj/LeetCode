class Router:

    def __init__(self, memoryLimit: int):
        self.S = set()
        self.A = deque()
        self.dest = defaultdict(deque)
        self.limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, source, destination) in self.S:
            return False
        if len(self.S) == self.limit:
            t,s,d = self.A.popleft()
            self.S.remove((t,s,d))
            self.dest[d].popleft()
        self.A.append((timestamp, source, destination))
        self.S.add((timestamp, source, destination))
        self.dest[destination].append([timestamp, source])
        return True

    def forwardPacket(self) -> List[int]:
        if self.S:
            t,s,d = self.A.popleft()
            self.S.remove((t,s,d))
            self.dest[d].popleft()
            return [s,d,t]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return bisect_right(self.dest[destination], [endTime,inf]) - bisect_left(self.dest[destination], [startTime,0])


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)