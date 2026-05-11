class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.max_tree = [-math.inf] * self.n
        self.max_tree.extend(arr)
        for i in range(self.n - 1, 0, -1):
            self.max_tree[i] = max(self.max_tree[i << 1], self.max_tree[i << 1 | 1])

    def update(self, i, val):
        i += self.n
        self.max_tree[i] = val
        while i > 1:
            self.max_tree[i >> 1] = max(self.max_tree[i], self.max_tree[i ^ 1])
            i >>= 1

    def max_val(self, l, r):
        maximum = -math.inf
        l += self.n
        r += self.n
        while l < r:
            if (l & 1):
                maximum = max(maximum, self.max_tree[l])
                l += 1
            if (r & 1):
                r -= 1
                maximum = max(maximum, self.max_tree[r])
            l >>= 1
            r >>= 1
        return maximum

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        A = sorted(set(nums))
        N = len(nums)
        T = SegmentTree([-inf]*N)
        T.update(bisect_left(A,nums[-1]), 0)
        for i in range(N-2,-1,-1):
            a = nums[i]-target
            b = nums[i]+target
            l = bisect_left(A, a)
            r = bisect_right(A, b)
            ma = T.max_val(l,r)
            T.update(bisect_left(A, nums[i]), ma+1)
        res = T.max_val(bisect_left(A, nums[0]), bisect_right(A, nums[0]))
        return res if res > -inf else -1