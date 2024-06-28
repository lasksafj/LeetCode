from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.A = SortedList()
        self.B = SortedList()

    def book(self, start: int, end: int) -> bool:
        A = self.A
        B = self.B
        
        p = A.bisect_right([start,end])
        if p > 0 and start < A[p-1][1]:
            p -= 1
        l = p
        nB = SortedList()
        while p < len(A) and A[p][0] <= end:
            s,e = A[p]
            s1,e1 = max(s,start), min(e,end)
            if s1 < e1:
                p1 = B.bisect_right([s1,e1])
                if (p1 > 0 and s1 < B[p1-1][1]) or (p1 < len(B) and B[p1][0] < e1):
                    return False
                nB.add([s1,e1])
            p += 1
        B.update(nB)
        if l < len(A):
            start = min(A[l][0],start)
        if p > 0:
            end = max(end, A[p-1][1])
        while l < p:
            A.pop(l)
            p -= 1
        A.add([start,end])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)