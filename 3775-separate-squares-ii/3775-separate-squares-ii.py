class SegTree:
    def __init__(self, tl, tr, nums):
        self.nums = nums
        self.tl = tl
        self.tr = tr
        self.cover = 0
        self.min_val = 0
        self.lazy = 0
        if tl < tr-1:
            mi = (tl+tr)//2
            self.left = SegTree(tl, mi, nums)
            self.right = SegTree(mi, tr, nums)
    
    def merge(self):
        if self.tl < self.tr-1:
            if self.min_val:
                self.cover = self.nums[self.tr] - self.nums[self.tl]
            else:
                self.cover = self.left.cover + self.right.cover
        elif self.tl == self.tr-1:
            self.cover = self.nums[self.tr] - self.nums[self.tl] if self.min_val else 0
    
    def push(self):
        if self.lazy == 0:
            return
        self.min_val += self.lazy
        if self.tl < self.tr-1:
            self.left.lazy += self.lazy
            self.right.lazy += self.lazy
        self.lazy = 0

    def update(self, l, r, inc):
        self.push()
        if r <= self.tl or self.tr <= l:
            return
        if l <= self.tl and self.tr <= r:
            self.min_val += inc
            self.push()
        else:
            # no need check self.tl < self.tr-1, b/c queries have at least 2 points
            self.left.update(l,r,inc)
            self.right.update(l,r,inc)
        self.merge()

    def query(self, l, r):
        self.push()
        if r <= self.tl or self.tr <= l:
            return 0
        if l <= self.tl and self.tr <= r:
            return self.cover
        return self.left.query(l,r) + self.right.query(l,r)

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        OPEN, CLOSE = 1, -1
        events = []
        Y_MAX = 0
        x_coor = set()
        for a,b,l in squares:
            events.append([b,a,a+l,OPEN])
            events.append([b+l,a,a+l,CLOSE])
            Y_MAX = max(Y_MAX, b+l)
            x_coor.add(a)
            x_coor.add(a+l)
        events.sort()
        x_coor = sorted(list(x_coor))
        mp = {x:i for i,x in enumerate(x_coor)}

        total = 0
        tally = []
        py = 0
        active = SegTree(0, len(x_coor)-1,x_coor)
        for y,x1,x2,typ in events:
            total += active.query(0, len(x_coor)-1) * (y - py)
            tally.append((y, total))
            
            l = mp[x1]
            r = mp[x2]
            if typ == OPEN:
                active.update(l,r,1)
            else:
                active.update(l,r,-1)
            py = y
        
        r = bisect_left(tally, total/2, key=lambda x: x[1])
        l = r-1

        (y,area), (Y,AREA) = tally[l], tally[r]
        slope = (AREA - area) / (Y - y)
        shift = (total/2 - area) / slope

        return y + shift