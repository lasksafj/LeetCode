from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.A = SortedList()

    def book(self, start: int, end: int) -> bool:
        A = self.A
        p = A.bisect_right([start,end])
        if (p > 0 and A[p-1][1] > start) or (p < len(A) and A[p][0] < end):
            return False
        A.add([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)