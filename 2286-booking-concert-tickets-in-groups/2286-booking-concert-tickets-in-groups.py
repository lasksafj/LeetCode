class BookMyShow:

    def __init__(self, n: int, m: int):
        self.Tree_max,self.Tree_sum = [m]*(2*n), [m]*(2*n)
        self.A = [m]*n
        self.m,self.n = m,n
        self.minRow = 0
        for i in range(n-1, 0, -1):
            self.Tree_sum[i] = self.Tree_sum[i<<1] + self.Tree_sum[i<<1^1]
            self.Tree_max[i] = max(self.Tree_max[i<<1], self.Tree_max[i<<1^1])
    
    def update(self, p, value):
        n = self.n
        t1,t2 = self.Tree_sum,self.Tree_max
        p += n
        t1[p] = value
        t2[p] = value
        while p > 1:
            t1[p>>1] = t1[p] + t1[p^1]
            t2[p>>1] = max(t2[p], t2[p^1])
            p >>= 1
    
    def get_sum(self, l,r):
        t = self.Tree_sum
        n = self.n
        res = 0
        l += n
        r += n
        while l < r:
            if l&1:
                res = res + t[l]
                l += 1
            if r&1:
                r -= 1
                res = res + t[r]
            l >>= 1
            r >>= 1
        return res
    
    def get_max(self, l,r):
        t = self.Tree_max
        n = self.n
        res = 0
        l += n
        r += n
        while l < r:
            if l&1:
                res = max(res , t[l])
                l += 1
            if r&1:
                r -= 1
                res = max(res , t[r])
            l >>= 1
            r >>= 1
        return res

    def gather(self, k: int, maxRow: int) -> List[int]:
        m,n = self.m,self.n
        T = self.Tree_max
        A = self.A
        l,r = 0,n
        # print('gather',A,T)
        while l < r:
            mi = (l+r)//2
            # print('gather', l,mi,r,self.get_max(0,mi))
            if self.get_max(0,mi+1) >= k:
                r = mi
            else:
                l = mi+1
        if l > maxRow:
            return []
        A[l] -= k
        self.update(l, A[l])
        return [l, m-(k+A[l])]

    def scatter(self, k: int, maxRow: int) -> bool:
        maxRow += 1
        if self.minRow >= maxRow:
            return False
        m,n = self.m,self.n
        A = self.A
        # print(A)
        # print(self.Tree_sum)
        if self.get_sum(0, maxRow) >= k:
            # print('scatter',self.get_sum(0, maxRow), k, maxRow)
            while k > 0 and self.minRow < n:
                # print(self.minRow)
                if k <= A[self.minRow]: 
                    A[self.minRow] -= k
                    k = 0
                else:
                    k -= A[self.minRow]
                    A[self.minRow] = 0
                self.update(self.minRow, A[self.minRow])
                if A[self.minRow] == 0:
                    self.minRow += 1
            return True
        return False

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)