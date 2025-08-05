class SegTree:
    def __init__(self, A):
        self.N = len(A)
        self.T = [inf]*(4*self.N)
        for i in range(self.N):
            self.update(i, A[i])
    def update(self, i, v):
        self.update_(i,v,1,0,self.N-1)
    def update_(self, i,v,t,l,r):
        if i < l or i > r:
            return
        if l == r:
            self.T[t] = v
            return
        mi = (l+r)//2
        if i <= mi:
            self.update_(i,v,t*2,l,mi)
        else:
            self.update_(i,v,t*2+1,mi+1,r)
        self.T[t] = min(self.T[t*2], self.T[t*2+1])
    def get(self, ql,qr):
        return self.get_(ql,qr, 1,0,self.N-1)
    def get_(self, ql,qr,t,l,r):
        if qr < l or r < ql:
            return inf
        if ql <= l and r <= qr:
            return self.T[t]
        mi = (l+r)//2
        return min(self.get_(ql,qr,t*2,l,mi), self.get_(ql,qr,t*2+1,mi+1,r))

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(baskets)
        A = sorted([[b,i] for i,b in enumerate(baskets)])
        mp = {}
        for k,(b,i) in enumerate(A):
            mp[i] = k
        T = SegTree([i for b,i in A])
        res = 0
        for f in fruits:
            l = bisect_left(A, f, key=lambda x:x[0])
            i = T.get(l, N-1)
            if i < inf:
                T.update(mp[i], inf)
            else:
                res += 1
        return res