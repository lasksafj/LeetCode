class SegTree:
    def __init__(self, N):
        self.N = N
        self.mi = [0]*(N*4)
        self.ma = [0]*(N*4)
        self.lazy = [0]*(N*4)
    def merge(self, i):
        self.mi[i] = min(self.mi[i*2], self.mi[i*2+1])
        self.ma[i] = max(self.ma[i*2], self.ma[i*2+1])
    def push(self, i, tl, tr):
        if self.lazy[i] != 0 and tl < tr:
            val = self.lazy[i]
            self.mi[i*2] += val
            self.ma[i*2] += val   
            self.mi[i*2+1] += val   
            self.ma[i*2+1] += val
            self.lazy[i*2] += val
            self.lazy[i*2+1] += val
            self.lazy[i] = 0
    def update(self, l, r, inc):
        def _update(i, tl, tr):
            self.push(i, tl, tr)
            if l <= tl and tr <= r:
                self.mi[i] += inc
                self.ma[i] += inc
                self.lazy[i] += inc
                return
            elif r < tl or tr < l:
                return
            mi = (tl+tr)//2
            _update(i*2, tl, mi)
            _update(i*2+1, mi+1, tr)
            self.merge(i)
        _update(1, 0, self.N-1)
    def find(self):
        def _find(i, tl, tr):
            self.push(i, tl, tr)
            if tl == tr:
                return tl if self.mi[i] <= 0 <= self.ma[i] else -1
            mi = (tl+tr)//2
            if self.mi[i*2+1] <= 0 <= self.ma[i*2+1]:
                return _find(i*2+1, mi+1, tr)
            return _find(i*2, tl, mi)
        return _find(1, 0, self.N-1)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        T = SegTree(len(nums))
        res = 0
        first = {}
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            inc = 1 if n&1 else -1
            if n in first:
                T.update(i, first[n]-1, inc)
                first[n] = i
            else:
                T.update(i, len(nums)-1, inc)
                first[n] = i
            j = T.find()
            res = max(res, j-i+1)
        return res