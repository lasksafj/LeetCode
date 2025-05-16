class SegTree:
    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.cnt = [0]*(self.N*4)
        self.cover = [0]*(self.N*4)

    def update(self, l, r, inc):
        self.update_(l, r, inc, 1, 0, self.N-1)
    
    def update_(self, l, r, inc, t, tl, tr):
        if r <= tl or tr <= l:
            return
        if l <= tl and tr <= r:
            self.cnt[t] += inc
        else:
            mi = (tl+tr)//2
            self.update_(l, r, inc, t*2, tl, mi)
            self.update_(l, r, inc, t*2+1, mi, tr)
        
        if tl+1 == tr:
            self.cover[t] = self.nums[tr] - self.nums[tl] if self.cnt[t] else 0
        else:
            if self.cnt[t]:
                self.cover[t] = self.nums[tr] - self.nums[tl]
            else:
                self.cover[t] = self.cover[t*2] + self.cover[t*2+1]

    def query(self):
        return self.cover[1]

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
        active = SegTree(x_coor)
        for y,x1,x2,typ in events:
            total += active.query() * (y - py)
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