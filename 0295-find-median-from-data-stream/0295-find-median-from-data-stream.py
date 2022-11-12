class MedianFinder:
    
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left == []:
            heapq.heappush(self.left, -num)
        else:
            if num <= -self.left[0]:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)
        while len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        while len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right) + 1:
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()