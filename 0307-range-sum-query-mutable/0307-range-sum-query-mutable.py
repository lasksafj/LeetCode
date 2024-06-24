class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.A = [0]*self.N
        self.T = [0]*(self.N+1)
        for i,n in enumerate(nums):
            self.update(i, n)

    def update(self, index: int, val: int) -> None:
        old_val = self.A[index]
        self.A[index] = val
        i = index+1
        while i <= self.N:
            self.T[i] += val-old_val
            i += i&(-i)
    
    def calc(self, index):
        res = 0
        i = index+1
        while i > 0:
            res += self.T[i]
            i -= i&(-i)
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.calc(right) - self.calc(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)