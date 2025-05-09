class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.A = SortedList()
        self.B = SortedList()
        self.C = SortedList()
        self.arr = deque()
        self.sum_B = 0
    
    def add(self, num):
        self.A.add(num)
        if len(self.A) > self.k:
            x = self.A.pop(-1)
            self.B.add(x)
            self.sum_B += x
        if len(self.B) > self.m-self.k*2:
            x = self.B.pop(-1)
            self.C.add(x)
            self.sum_B -= x
    
    def remove(self, num):
        if num <= self.A[-1]:
            self.A.remove(num)
        elif num <= self.B[-1]:
            self.sum_B -= num
            self.B.remove(num)
        else:
            self.C.remove(num)
        if len(self.A) < self.k:
            x = self.B.pop(0)
            self.A.add(x)
            self.sum_B -= x
        if len(self.B) < self.m-self.k*2:
            x = self.C.pop(0)
            self.B.add(x)
            self.sum_B += x

    def addElement(self, num: int) -> None:
        self.arr.append(num)
        if len(self.arr) > self.m:
            x = self.arr.popleft()
            self.remove(x)
        self.add(num)

    def calculateMKAverage(self) -> int:
        if len(self.arr) < self.m:
            return -1
        return self.sum_B // len(self.B)        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()