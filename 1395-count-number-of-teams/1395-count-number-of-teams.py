class NumArray:
    def __init__(self, N):
        self.N = N
        self.T = [0]*(self.N+1)
        

    def update(self, index: int, val: int) -> None:
        i = index+1
        while i <= self.N:
            self.T[i] += val
            i += i&(-i)
    
    def calc(self, index):
        res = 0
        i = index+1
        while i > 0:
            res += self.T[i]
            i -= i&(-i)
        return res

from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def sol(rating):
            N = len(rating)
            T = NumArray(max(rating)+1)
            A = SortedList([])
            res = 0
            for r in rating:
                res += T.calc(r-1)
                T.update(r, A.bisect_right(r-1))
                A.add(r)
            return res
        return sol(rating) + sol(rating[::-1])