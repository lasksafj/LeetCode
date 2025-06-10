class SegTree:
    def __init__(self, l, r, k, nums):
        self.k = k
        self.l = l
        self.r = r
        self.cnt = [0]*k
        if l < r:
            mi = (l+r)//2
            self.left = SegTree(l, mi, k, nums)
            self.right = SegTree(mi+1, r, k, nums)
            self.merge()
        else:
            self.p = nums[l]%k
            self.cnt[nums[l]%k] = 1
    def merge(self):
        self.p = (self.left.p * self.right.p) % self.k
        for r in range(self.k):
            self.cnt[r] = self.left.cnt[r]
        for r in range(self.k):
            self.cnt[(r * self.left.p) % self.k] += self.right.cnt[r]
    def update(self, i, v):
        if self.l == self.r:
            self.cnt = [0]*self.k
            self.p = v%self.k
            self.cnt[v%self.k] = 1
            return
        mi = (self.l + self.r)//2
        if i <= mi:
            self.left.update(i, v)
        else:
            self.right.update(i,v)
        self.merge()
    def query(self, ql, qr):
        cnt = [0]*self.k
        if self.r < ql or qr < self.l:
            return [1, cnt]
        if ql <= self.l and self.r <= qr:
            return [self.p,self.cnt]
        mi = (self.l + self.r)//2

        lp,lcnt = self.left.query(ql,qr)
        rp,rcnt = self.right.query(ql,qr)
        
        p = (lp * rp) % self.k
        for r in range(self.k):
            cnt[r] = lcnt[r]
        for r in range(self.k):
            cnt[(r * lp) % self.k] += rcnt[r]
        return [p,cnt]

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        N = len(nums)
        T = SegTree(0, N-1, k, nums)
        res = []
        for i,v,start,x in queries:
            T.update(i,v)
            res.append(T.query(start, N-1)[1][x])
        return res