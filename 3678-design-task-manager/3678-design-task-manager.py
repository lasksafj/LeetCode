class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.SL = SortedList([], key=lambda t: [self.P[t], t])
        self.P = {}
        self.U = {}
        for u,t,p in tasks:
            self.add(u,t,p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.P[taskId] = priority
        self.U[taskId] = userId
        self.SL.add(taskId)

    def edit(self, taskId: int, newPriority: int) -> None:
        self.SL.remove(taskId)
        self.P[taskId] = newPriority
        self.SL.add(taskId)

    def rmv(self, taskId: int) -> None:
        self.SL.remove(taskId)
        del self.P[taskId]
        del self.U[taskId]

    def execTop(self) -> int:
        if not self.SL:
            return -1
        t = self.SL[-1]
        u = self.U[t]
        self.rmv(t)
        return u


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()