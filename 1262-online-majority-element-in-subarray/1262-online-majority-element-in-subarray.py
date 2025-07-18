class SegTree:
    def __init__(self, left, right, nums) -> None:
        self.left = left
        self.right = right
        self.val = nums[left]
        self.cnt = 1
        if left < right:
            mi = (left + right)//2
            self.lchild = SegTree(left, mi, nums)
            self.rchild = SegTree(mi+1, right, nums)
            self.val, self.cnt = self.calc([self.lchild.val, self.lchild.cnt], [self.rchild.val, self.rchild.cnt])
    
    def calc(self, a,b):
        if self.left == self.right:
            return
        aval,acnt = a
        bval,bcnt = b
        if aval == bval:
            return aval, acnt+bcnt
        elif acnt > bcnt:
            return aval, acnt-bcnt
        return bval, bcnt-acnt
    
    def query(self, l, r):
        if l > self.right or r < self.left:
            return [0,0]
        if l <= self.left and self.right <= r:
            return self.val, self.cnt
        return self.calc(self.lchild.query(l, r), self.rchild.query(l, r))

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.T = SegTree(0, len(arr)-1, arr)
        self.P = defaultdict(list)
        for i,a in enumerate(arr):
            self.P[a].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        val = self.T.query(left, right)[0]
        if bisect_right(self.P[val], right) - bisect_left(self.P[val], left) >= threshold:
            return val
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)